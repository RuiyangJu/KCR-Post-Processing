from __future__ import annotations

import argparse
import glob
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = BASE_DIR
MODEL_ROOT_DIR = os.path.join(PROJECT_DIR, "model")
ZERO_SHOT_DIR = os.path.join(PROJECT_DIR, "zero_shot")
REFINER_DIR = os.path.join(PROJECT_DIR, "refiner")
DEFAULT_INPUT_DIR = os.path.join(PROJECT_DIR, "dataset", "valid", "input")

DEFAULT_SYSTEM_PROMPT = """\
あなたは日本古典籍OCRの誤り訂正システムです。

OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
修正後の本文のみを出力してください。
"""

RAKUTEN_CHAT_TEMPLATE = (
    "A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's "
    "questions. USER: "
    "{{ messages[0]['content'] | trim }}\n\n"
    "{{ messages[1]['content'] | trim }} ASSISTANT:"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a base or LoRA-refined OCR model on txt files.")
    model_group = parser.add_mutually_exclusive_group(required=True)
    model_group.add_argument("--model-name")
    model_group.add_argument("--model-dir")
    parser.add_argument("--adapter-dir")
    parser.add_argument("--no-adapter", action="store_true")
    parser.add_argument("--input-dir", default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir")
    parser.add_argument("--max-new-tokens", type=int, default=1024)

    return parser.parse_args()


def load_runtime_libraries(use_adapter: bool) -> None:
    global AutoModelForCausalLM
    global AutoTokenizer
    global PeftModel
    global torch

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    if use_adapter:
        from peft import PeftModel


def model_family_name(model_dir: str) -> str:
    normalized_model_dir = os.path.normpath(model_dir)
    basename = os.path.basename(normalized_model_dir)

    if basename == "model":
        return os.path.basename(os.path.dirname(normalized_model_dir)).lower()

    return basename.lower()


def resolve_model_dir(args: argparse.Namespace) -> str:
    if args.model_name:
        model_candidates = (
            os.path.join(MODEL_ROOT_DIR, args.model_name),
            os.path.join(ZERO_SHOT_DIR, args.model_name, "model"),
        )

        model_dir = next(
            (candidate for candidate in model_candidates if os.path.isdir(candidate)),
            model_candidates[0],
        )
        return os.path.abspath(model_dir)

    return os.path.abspath(args.model_dir)


def adapter_dir_candidates(args: argparse.Namespace, model_dir: str) -> list[str]:
    candidates = []

    if args.model_name:
        candidates.extend(
            [
                # Common training output layout:
                # refiner/<model-name>/model/adapter_config.json
                os.path.join(REFINER_DIR, args.model_name, "model"),
                os.path.join(REFINER_DIR, args.model_name, "refiner_lora"),
                os.path.join(REFINER_DIR, args.model_name),
            ]
        )

    if os.path.basename(os.path.normpath(model_dir)) == "model":
        model_root = os.path.dirname(model_dir)
    else:
        model_root = model_dir

    candidates.extend(
        [
            os.path.join(model_root, "model"),
            os.path.join(model_root, "refiner_lora"),
        ]
    )

    # Keep order while removing duplicate paths.
    unique_candidates = []
    seen = set()
    for candidate in candidates:
        candidate = os.path.abspath(candidate)
        if candidate not in seen:
            unique_candidates.append(candidate)
            seen.add(candidate)

    return unique_candidates


def is_adapter_dir(path: str) -> bool:
    return os.path.isdir(path) and os.path.isfile(
        os.path.join(path, "adapter_config.json")
    )


def resolve_explicit_adapter_dir(adapter_dir: str) -> str:
    adapter_dir = os.path.abspath(adapter_dir)

    candidates = [
        adapter_dir,
        os.path.join(adapter_dir, "model"),
        os.path.join(adapter_dir, "refiner_lora"),
    ]

    adapter_dir = next(
        (candidate for candidate in candidates if is_adapter_dir(candidate)),
        adapter_dir,
    )

    return os.path.abspath(adapter_dir)


def resolve_adapter_dir(
    args: argparse.Namespace,
    model_dir: str,
) -> str | None:
    if args.no_adapter:
        return None

    if args.adapter_dir:
        return resolve_explicit_adapter_dir(args.adapter_dir)

    adapter_dir = next(
        (
            candidate
            for candidate in adapter_dir_candidates(args, model_dir)
            if is_adapter_dir(candidate)
        ),
        None,
    )

    if adapter_dir:
        return os.path.abspath(adapter_dir)

    return os.path.abspath(adapter_dir_candidates(args, model_dir)[0])


def resolve_output_dir(
    args: argparse.Namespace,
    model_dir: str,
    adapter_dir: str | None,
) -> str:
    if args.output_dir:
        return os.path.abspath(args.output_dir)

    model_root = (
        os.path.dirname(model_dir)
        if os.path.basename(os.path.normpath(model_dir)) == "model"
        else model_dir
    )
    output_name = "output_refiner_valid" if adapter_dir else "output_base_valid"

    return os.path.join(model_root, output_name)


def prompt_style_for(model_dir: str) -> str:
    return "user-only" if "gemma" in model_family_name(model_dir) else "system-user"


def is_qwen_model(model_dir: str) -> bool:
    return "qwen" in model_family_name(model_dir)


def eos_token_ids(tokenizer) -> int | list[int] | None:
    token_ids = []
    model_eos_token_id = tokenizer.eos_token_id

    if isinstance(model_eos_token_id, int):
        token_ids.append(model_eos_token_id)
    elif isinstance(model_eos_token_id, list):
        token_ids.extend(model_eos_token_id)

    if hasattr(tokenizer, "convert_tokens_to_ids"):
        for special_token in ("<|end_of_text|>", "<|eot_id|>"):
            token_id = tokenizer.convert_tokens_to_ids(special_token)

            if isinstance(token_id, int) and token_id >= 0:
                token_ids.append(token_id)

    token_ids = sorted(set(token_ids))

    if not token_ids:
        return None

    if len(token_ids) == 1:
        return token_ids[0]

    return token_ids


def configure_tokenizer(tokenizer, model_dir: str) -> None:
    if tokenizer.chat_template is None and "rakuten" in model_family_name(model_dir):
        tokenizer.chat_template = RAKUTEN_CHAT_TEMPLATE

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "right"


def build_messages(ocr_text: str, model_dir: str) -> list[dict[str, str]]:
    if prompt_style_for(model_dir) == "user-only":
        return [
            {
                "role": "user",
                "content": f"{DEFAULT_SYSTEM_PROMPT}\n{ocr_text}",
            }
        ]

    return [
        {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
        {"role": "user", "content": ocr_text},
    ]


def apply_chat_template(
    tokenizer,
    messages: list[dict[str, str]],
    model_dir: str,
) -> str:
    kwargs = {
        "tokenize": False,
        "add_generation_prompt": True,
    }

    if is_qwen_model(model_dir):
        kwargs["enable_thinking"] = False

    try:
        return tokenizer.apply_chat_template(messages, **kwargs)
    except TypeError:
        kwargs.pop("enable_thinking", None)
        return tokenizer.apply_chat_template(messages, **kwargs)


def main() -> None:
    args = parse_args()
    model_dir = resolve_model_dir(args)
    adapter_dir = resolve_adapter_dir(args, model_dir)
    output_dir = resolve_output_dir(args, model_dir, adapter_dir)

    if not os.path.isdir(model_dir):
        raise FileNotFoundError(f"Model directory not found: {model_dir}")

    if adapter_dir and not is_adapter_dir(adapter_dir):
        checked_paths = (
            [resolve_explicit_adapter_dir(args.adapter_dir)]
            if args.adapter_dir
            else adapter_dir_candidates(args, model_dir)
        )
        checked_paths_text = "\n  - ".join(checked_paths)
        raise FileNotFoundError(
            "Adapter directory is invalid or missing adapter_config.json.\n"
            f"Resolved adapter directory: {adapter_dir}\n"
            f"Checked candidates:\n  - {checked_paths_text}"
        )

    if not os.path.isdir(args.input_dir):
        raise FileNotFoundError(f"Input directory not found: {args.input_dir}")

    load_runtime_libraries(use_adapter=adapter_dir is not None)

    os.makedirs(output_dir, exist_ok=True)

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    configure_tokenizer(tokenizer, model_dir)

    pad_token_id = (
        tokenizer.pad_token_id
        if tokenizer.pad_token_id is not None
        else tokenizer.eos_token_id
    )
    eos_token_id = eos_token_ids(tokenizer)

    print("Loading base model...")
    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        torch_dtype="auto",
        device_map={"": "cuda:0"},
        attn_implementation="sdpa",
        trust_remote_code=True,
    )

    if adapter_dir:
        print(f"Loading adapter: {adapter_dir}")
        model = PeftModel.from_pretrained(model, adapter_dir)
    else:
        print("Running base model without adapter.")

    model.eval()

    txt_files = sorted(glob.glob(os.path.join(args.input_dir, "*.txt")))

    print(f"Input directory: {args.input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Found {len(txt_files)} files.")

    inference_times = []

    for idx, txt_path in enumerate(txt_files, start=1):
        filename = os.path.basename(txt_path)
        output_path = os.path.join(output_dir, filename)

        with open(txt_path, "r", encoding="utf-8") as f:
            ocr_text = f.read().strip()

        prompt = apply_chat_template(
            tokenizer,
            build_messages(ocr_text, model_dir),
            model_dir,
        )
        input_ids = tokenizer.encode(
            prompt,
            add_special_tokens=False,
            return_tensors="pt",
        ).to(model.device)

        if torch.cuda.is_available():
            torch.cuda.synchronize()

        start_time = time.perf_counter()

        with torch.inference_mode():
            output_ids = model.generate(
                input_ids,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
                pad_token_id=pad_token_id,
                eos_token_id=eos_token_id,
            )

        if torch.cuda.is_available():
            torch.cuda.synchronize()

        inference_time = time.perf_counter() - start_time
        inference_times.append(inference_time)

        corrected_text = tokenizer.decode(
            output_ids[0][input_ids.size(1):],
            skip_special_tokens=True,
        ).strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(corrected_text)

        print(
            f"[{idx}/{len(txt_files)}] "
            f"Saved: {output_path} ({inference_time:.3f} s)"
        )

    if inference_times:
        print(
            "Average inference time: "
            f"{sum(inference_times) / len(inference_times):.3f} s/file"
        )


if __name__ == "__main__":
    main()
