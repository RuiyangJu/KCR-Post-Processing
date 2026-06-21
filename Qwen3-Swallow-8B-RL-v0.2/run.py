import glob
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
INPUT_DIR = os.path.join(BASE_DIR, "..", "dataset", "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

DEFAULT_SYSTEM_PROMPT = """\
あなたは日本古典籍OCRの誤り訂正システムです。

OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
修正後の本文のみを出力してください。
"""

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR,
    torch_dtype="auto",
    device_map={"": "cuda:0"},
    attn_implementation="sdpa",
)
model.eval()

print("Model loaded.")


def correct_ocr_text(ocr_text: str) -> tuple[str, float]:
    messages = [
        {
            "role": "system",
            "content": DEFAULT_SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": ocr_text,
        },
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    token_ids = tokenizer.encode(
        prompt,
        add_special_tokens=False,
        return_tensors="pt",
    ).to(model.device)

    if torch.cuda.is_available():
        torch.cuda.synchronize()
    start_time = time.perf_counter()

    with torch.inference_mode():
        output_ids = model.generate(
            token_ids,
            max_new_tokens=1024,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    if torch.cuda.is_available():
        torch.cuda.synchronize()
    inference_time = time.perf_counter() - start_time

    corrected_text = tokenizer.decode(
        output_ids[0][token_ids.size(1) :],
        skip_special_tokens=True,
    )

    return corrected_text.strip(), inference_time


txt_files = sorted(glob.glob(os.path.join(INPUT_DIR, "*.txt")))

print(f"Found {len(txt_files)} files.")

inference_times = []

for idx, txt_path in enumerate(txt_files, start=1):
    filename = os.path.basename(txt_path)
    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(txt_path, "r", encoding="utf-8") as f:
        ocr_text = f.read().strip()

    corrected_text, inference_time = correct_ocr_text(ocr_text)
    inference_times.append(inference_time)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(corrected_text)

    print(
        f"[{idx}/{len(txt_files)}] Saved: {output_path} "
        f"(inference: {inference_time:.3f} s)"
    )

if inference_times:
    total_inference_time = sum(inference_times)
    average_inference_time = total_inference_time / len(inference_times)
    print(f"Total inference time: {total_inference_time:.3f} s")
    print(f"Average inference time: {average_inference_time:.3f} s/file")

print("Done.")
