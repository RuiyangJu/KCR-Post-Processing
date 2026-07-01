## LLM-based OCR Refiner Fine-tuning
### Fine-tune & Run & Evaluate: Synthetic Test Set Example
First, move to the repository root:
```
cd KCR-Post-Processing
```

#### Batch Fine-tune & Run & Evaluate
Fine-tune all eight LLM models on the training and validation sets, then run inference and evaluate them on both the real and synthetic test sets:

```
  bash run_refiner.sh
```

#### (1) [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06)

```bash
  python refiner.py \
    --model-name Llama-3.1-Swallow-8B-Instruct-v0.3

  python run.py \
    --model-name Llama-3.1-Swallow-8B-Instruct-v0.3 \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Llama-3.1-Swallow-8B-Instruct-v0.3/output_refiner_synth

  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Llama-3.1-Swallow-8B-Instruct-v0.3/output_refiner_synth \
    --out_csv zero_shot/Llama-3-ELYZA-JP-8B/output_refiner_synthetic_cer.csv
```

#### (2) [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) (Release: 2025/03)


#### (3) [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07)


#### (4) [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12)


#### (5) [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03)

#### (6) [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05)


#### (7) [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02)


#### (8) [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04)

