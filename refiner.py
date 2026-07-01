from __future__ import annotations

import argparse
import inspect
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
ZERO_SHOT_DIR = os.path.join(BASE_DIR, "zero_shot")
REFINER_DIR = os.path.join(BASE_DIR, "refiner")
DEFAULT_TRAIN_INPUT_DIR = os.path.join(BASE_DIR, "dataset", "train", "input")
DEFAULT_TRAIN_TARGET_DIR = os.path.join(BASE_DIR, "dataset", "train", "gt")
DEFAULT_VALID_INPUT_DIR = os.path.join(BASE_DIR, "dataset", "valid", "input")
DEFAULT_VALID_TARGET_DIR = os.path.join(BASE_DIR, "dataset", "valid", "gt")

DEFAULT_SYSTEM_PROMPT = """\
あなたは日本古典籍OCRの誤り訂正システムです。

OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
修正後の本文のみを出力してください。
"""

YOLO_LABEL_RE = re.compile(r"^\s*\d+(?:\s+[-+]?\d*\.?\d+){4}\s*$")

RAKUTEN_CHAT_TEMPLATE = (
    "A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's "
    "questions. USER: "
    "{{ messages[0]['content'] | trim }}\n\n"
    "{{ messages[1]['content'] | trim }} ASSISTANT:"
)


def model_family_name(model_dir: str) -> str:
    normalized_model_dir = os.path.normpath(model_dir)
    basename = os.path.basename(normalized_model_dir)
    if basename == "model":
        return os.path.basename(os.path.dirname(normalized_model_dir)).lower()
    return basename.lower()


def model_output_name(args: argparse.Namespace, model_dir: str) -> str:
    if args.model_name:
        return args.model_name

    normalized_model_dir = os.path.normpath(model_dir)
    basename = os.path.basename(normalized_model_dir)
    if basename == "model":
        return os.path.basename(os.path.dirname(normalized_model_dir))
    return basename


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a LoRA OCR refiner for any zero_shot model directory.")
    model_group = parser.add_mutually_exclusive_group(required=True)
    model_group.add_argument("--model-name")
    model_group.add_argument("--model-dir")
    parser.add_argument("--train-input-dir", default=DEFAULT_TRAIN_INPUT_DIR)
    parser.add_argument("--train-target-dir", "--train-gt-dir", dest="train_target_dir", default=DEFAULT_TRAIN_TARGET_DIR)
    parser.add_argument("--valid-input-dir", default=DEFAULT_VALID_INPUT_DIR)
    parser.add_argument("--valid-target-dir", "--valid-gt-dir", dest="valid_target_dir", default=DEFAULT_VALID_TARGET_DIR)
    parser.add_argument("--output-dir", "--refiner-output-dir", "--lora-output-dir", dest="output_dir")
    parser.add_argument("--prompt-style", choices=("auto", "system-user", "user-only"), default="auto")
    parser.add_argument("--max-length", type=int, default=1024)
    parser.add_argument("--num-train-epochs", type=float, default=5)
    parser.add_argument("--per-device-train-batch-size", type=int, default=4)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=5e-5)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--eval-steps", type=int, default=25)
    parser.add_argument("--save-steps", type=int, default=25)
    parser.add_argument("--logging-steps", type=int, default=10)
    parser.add_argument("--save-total-limit", type=int, default=5)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.1)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--no-bf16", action="store_true")
    parser.add_argument("--no-gradient-checkpointing", action="store_true")
    parser.add_argument("--strict-pairs", action="store_true")
    parser.add_argument("--check-data-only", action="store_true")
    return parser.parse_args()


def load_training_libraries() -> None:
    global AutoModelForCausalLM
    global AutoTokenizer
    global BitsAndBytesConfig
    global LoraConfig
    global Trainer
    global TrainingArguments
    global get_peft_model
    global prepare_model_for_kbit_training
    global torch

    import torch
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        BitsAndBytesConfig,
        Trainer,
        TrainingArguments,
    )


def infer_prompt_style(model_dir: str, requested_style: str) -> str:
    if requested_style != "auto":
        return requested_style

    model_name = model_family_name(model_dir)
    if "gemma" in model_name:
        return "user-only"
    return "system-user"


def is_qwen_model(model_dir: str) -> bool:
    model_name = model_family_name(model_dir)
    return "qwen" in model_name


def configure_tokenizer(tokenizer: AutoTokenizer, model_dir: str) -> None:
    model_name = model_family_name(model_dir)
    if tokenizer.chat_template is None and "rakuten" in model_name:
        tokenizer.chat_template = RAKUTEN_CHAT_TEMPLATE
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"


def resolve_model_dir(args: argparse.Namespace) -> str:
    if args.model_name:
        model_candidates = [
            os.path.join(MODEL_DIR, args.model_name),
            os.path.join(ZERO_SHOT_DIR, args.model_name, "model"),
        ]
        model_dir = next(
            (candidate for candidate in model_candidates if os.path.isdir(candidate)),
            model_candidates[0],
        )
    else:
        model_dir = args.model_dir

    model_dir = os.path.abspath(model_dir)
    if not os.path.isdir(model_dir):
        raise FileNotFoundError(f"Model directory not found: {model_dir}")
    return model_dir


def resolve_output_dir(args: argparse.Namespace, model_dir: str) -> str:
    if args.output_dir:
        return os.path.abspath(args.output_dir)

    return os.path.join(REFINER_DIR, model_output_name(args, model_dir), "model")


def validate_txt_dirs(args: argparse.Namespace) -> None:
    for dir_path in (
        args.train_input_dir,
        args.train_target_dir,
        args.valid_input_dir,
        args.valid_target_dir,
    ):
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"Text directory not found: {dir_path}")


def validate_target_text_files(args: argparse.Namespace) -> None:
    for split_name, target_dir in (
        ("train", args.train_target_dir),
        ("validation", args.valid_target_dir),
    ):
        target_root = Path(target_dir)
        yolo_like_targets = [
            path.name
            for path in sorted(target_root.glob("*.txt"))
            if looks_like_yolo_labels(read_text(path))
        ]
        if yolo_like_targets:
            preview = ", ".join(yolo_like_targets[:5])
            raise ValueError(
                f"{split_name}: {len(yolo_like_targets)} target files look like YOLO label "
                f"coordinates, not OCR correction text. Check {target_root}. Examples: {preview}"
            )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def looks_like_yolo_labels(text: str) -> bool:
    lines = [line for line in text.splitlines() if line.strip()]
    return bool(lines) and all(YOLO_LABEL_RE.match(line) for line in lines)


def load_txt_pairs(
    input_dir: str,
    target_dir: str,
    split_name: str,
    strict_pairs: bool,
) -> list[dict[str, str]]:
    input_root = Path(input_dir)
    target_root = Path(target_dir)
    input_paths = sorted(input_root.glob("*.txt"))
    if not input_paths:
        raise ValueError(f"No .txt files found in {input_root}")

    rows = []
    missing_targets = []
    yolo_like_targets = []
    for input_path in input_paths:
        target_path = target_root / input_path.name
        if not target_path.exists():
            missing_targets.append(input_path.name)
            continue
        target_text = read_text(target_path)
        if looks_like_yolo_labels(target_text):
            yolo_like_targets.append(input_path.name)
            continue
        rows.append(
            {
                "id": input_path.stem,
                "input": read_text(input_path),
                "output": target_text,
            }
        )

    if missing_targets:
        preview = ", ".join(missing_targets[:5])
        message = (
            f"{split_name}: missing {len(missing_targets)} target txt files in "
            f"{target_root}. Examples: {preview}"
        )
        if strict_pairs:
            raise FileNotFoundError(message)
        print(f"Warning: {message}. Skipping these inputs.")

    if yolo_like_targets:
        preview = ", ".join(yolo_like_targets[:5])
        raise ValueError(
            f"{split_name}: {len(yolo_like_targets)} target files look like YOLO label "
            f"coordinates, not OCR correction text. Check {target_root}. Examples: {preview}"
        )

    target_names = {path.name for path in target_root.glob("*.txt")}
    extra_targets = sorted(target_names - {path.name for path in input_paths})
    if extra_targets:
        preview = ", ".join(extra_targets[:5])
        raise ValueError(
            f"{split_name}: found {len(extra_targets)} target files without input files. "
            f"Examples: {preview}"
        )

    return rows


class RefinerTokenizedDataset:
    def __init__(
        self,
        rows: list[dict[str, str]],
        tokenizer: AutoTokenizer,
        prompt_style: str,
        max_length: int,
        enable_thinking: bool,
    ) -> None:
        self.rows = rows
        self.tokenizer = tokenizer
        self.prompt_style = prompt_style
        self.max_length = max_length
        self.enable_thinking = enable_thinking

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int) -> dict[str, list[int]]:
        return tokenize_example(
            self.rows[index],
            self.tokenizer,
            self.prompt_style,
            self.max_length,
            self.enable_thinking,
        )


def load_refiner_rows(args: argparse.Namespace) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    train_rows = load_txt_pairs(
        args.train_input_dir,
        args.train_target_dir,
        "train",
        args.strict_pairs,
    )
    valid_rows = load_txt_pairs(
        args.valid_input_dir,
        args.valid_target_dir,
        "validation",
        args.strict_pairs,
    )
    print(f"Loaded {len(train_rows)} train pairs and {len(valid_rows)} validation pairs.")
    return train_rows, valid_rows


def extract_pair(example: dict[str, Any]) -> tuple[str, str]:
    return str(example["input"]).strip(), str(example["output"]).strip()


def build_messages(input_text: str, target_text: str | None, prompt_style: str) -> list[dict[str, str]]:
    if prompt_style == "user-only":
        messages = [
            {
                "role": "user",
                "content": f"{DEFAULT_SYSTEM_PROMPT}\n{input_text}",
            }
        ]
    else:
        messages = [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": input_text},
        ]

    if target_text is not None:
        messages.append({"role": "assistant", "content": target_text})
    return messages


def apply_chat_template(tokenizer: AutoTokenizer, messages: list[dict[str, str]], *, add_generation_prompt: bool, enable_thinking: bool) -> str:
    kwargs = {
        "tokenize": False,
        "add_generation_prompt": add_generation_prompt,
    }
    if enable_thinking is False:
        kwargs["enable_thinking"] = False

    try:
        return tokenizer.apply_chat_template(messages, **kwargs)
    except TypeError:
        kwargs.pop("enable_thinking", None)
        return tokenizer.apply_chat_template(messages, **kwargs)


def tokenize_example(
    example: dict[str, Any],
    tokenizer: AutoTokenizer,
    prompt_style: str,
    max_length: int,
    enable_thinking: bool,
) -> dict[str, list[int]]:
    input_text, target_text = extract_pair(example)

    prompt = apply_chat_template(
        tokenizer,
        build_messages(input_text, None, prompt_style),
        add_generation_prompt=True,
        enable_thinking=enable_thinking,
    )
    full_text = apply_chat_template(
        tokenizer,
        build_messages(input_text, target_text, prompt_style),
        add_generation_prompt=False,
        enable_thinking=enable_thinking,
    )

    prompt_ids = tokenizer(
        prompt,
        add_special_tokens=False,
        truncation=True,
        max_length=max_length,
    )["input_ids"]
    full_ids = tokenizer(
        full_text,
        add_special_tokens=False,
        truncation=True,
        max_length=max_length,
    )["input_ids"]

    prompt_len = min(len(prompt_ids), len(full_ids))
    labels = [-100] * prompt_len + full_ids[prompt_len:]
    if all(label == -100 for label in labels):
        raise ValueError(
            "The target text was fully truncated. Increase --max-length or shorten inputs."
        )

    return {
        "input_ids": full_ids,
        "attention_mask": [1] * len(full_ids),
        "labels": labels,
    }


@dataclass
class DataCollatorForCausalRefiner:
    tokenizer: AutoTokenizer

    def __call__(self, features: list[dict[str, list[int]]]) -> dict[str, torch.Tensor]:
        max_length = max(len(feature["input_ids"]) for feature in features)
        pad_token_id = self.tokenizer.pad_token_id

        batch = {
            "input_ids": [],
            "attention_mask": [],
            "labels": [],
        }
        for feature in features:
            pad_length = max_length - len(feature["input_ids"])
            batch["input_ids"].append(feature["input_ids"] + [pad_token_id] * pad_length)
            batch["attention_mask"].append(feature["attention_mask"] + [0] * pad_length)
            batch["labels"].append(feature["labels"] + [-100] * pad_length)

        return {
            key: torch.tensor(value, dtype=torch.long)
            for key, value in batch.items()
        }


def build_training_arguments(args: argparse.Namespace) -> TrainingArguments:
    use_fp16 = args.fp16
    use_bf16 = not args.no_bf16 and not use_fp16
    kwargs = {
        "output_dir": args.output_dir,
        "num_train_epochs": args.num_train_epochs,
        "per_device_train_batch_size": args.per_device_train_batch_size,
        "per_device_eval_batch_size": args.per_device_eval_batch_size,
        "gradient_accumulation_steps": args.gradient_accumulation_steps,
        "learning_rate": args.learning_rate,
        "warmup_ratio": args.warmup_ratio,
        "lr_scheduler_type": "cosine",
        "optim": "paged_adamw_8bit",
        "max_grad_norm": 0.3,
        "weight_decay": 0.0,
        "logging_steps": args.logging_steps,
        "eval_steps": args.eval_steps,
        "save_strategy": "steps",
        "save_steps": args.save_steps,
        "save_total_limit": args.save_total_limit,
        "load_best_model_at_end": True,
        "metric_for_best_model": "eval_loss",
        "greater_is_better": False,
        "bf16": use_bf16,
        "fp16": use_fp16,
        "gradient_checkpointing": not args.no_gradient_checkpointing,
        "report_to": "none",
    }
    if "eval_strategy" in inspect.signature(TrainingArguments.__init__).parameters:
        kwargs["eval_strategy"] = "steps"
    else:
        kwargs["evaluation_strategy"] = "steps"

    return TrainingArguments(**kwargs)


def main() -> None:
    args = parse_args()
    model_dir = resolve_model_dir(args)
    output_dir = resolve_output_dir(args, model_dir)

    validate_txt_dirs(args)
    validate_target_text_files(args)

    if args.check_data_only:
        train_rows = load_txt_pairs(
            args.train_input_dir,
            args.train_target_dir,
            "train",
            args.strict_pairs,
        )
        valid_rows = load_txt_pairs(
            args.valid_input_dir,
            args.valid_target_dir,
            "validation",
            args.strict_pairs,
        )
        print(f"Train pairs: {len(train_rows)}")
        print(f"Validation pairs: {len(valid_rows)}")
        return

    load_training_libraries()

    prompt_style = infer_prompt_style(model_dir, args.prompt_style)
    enable_thinking = not is_qwen_model(model_dir)
    compute_dtype = torch.float16 if args.fp16 or args.no_bf16 else torch.bfloat16

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_dir,
        trust_remote_code=True,
    )
    configure_tokenizer(tokenizer, model_dir)

    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )
    model.config.use_cache = False

    if not args.no_gradient_checkpointing:
        model.gradient_checkpointing_enable()

    model = prepare_model_for_kbit_training(
        model,
        use_gradient_checkpointing=not args.no_gradient_checkpointing,
    )

    peft_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
        ],
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    train_rows, valid_rows = load_refiner_rows(args)
    train_dataset = RefinerTokenizedDataset(
        train_rows,
        tokenizer,
        prompt_style,
        args.max_length,
        enable_thinking,
    )
    valid_dataset = RefinerTokenizedDataset(
        valid_rows,
        tokenizer,
        prompt_style,
        args.max_length,
        enable_thinking,
    )

    args.output_dir = output_dir
    training_args = build_training_arguments(args)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        data_collator=DataCollatorForCausalRefiner(tokenizer),
    )

    print(f"Model dir: {model_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Prompt style: {prompt_style}")
    print(f"Qwen thinking disabled: {not enable_thinking}")
    print(f"Max length: {args.max_length}")

    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)


if __name__ == "__main__":
    main()
