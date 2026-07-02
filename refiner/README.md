## LLM-based OCR Refiner Fine-tuning
### Fine-tuning Parameters
| Parameter | Setting |
| :--: | :--: |
| `max_length` | `2048` |
| `num_train_epochs` | `5` |
| `per_device_train_batch_size` | `4` |
| `per_device_eval_batch_size` | `2` |
| `gradient_accumulation_steps` | `8` |
| `learning_rate` | `5e-5` |
| `warmup_ratio` | `0.03` |
| `eval_steps` | `25` |
| `save_steps` | `25` |
| `logging_steps` | `10` |
| `save_total_limit` | `5` |
| `lora_r` | `16` |
| `lora_alpha` | `32` |
| `lora_dropout` | `0.1` |

### Fine-tune & Run & Evaluate: Synthetic Test Set Example
First, move to the repository root:
```bash
  cd KCR-Post-Processing
```

#### Batch Fine-tune, Run, and Evaluate
Fine-tune all eight LLM models on the training and validation sets, then run inference and evaluate them on both the real and synthetic test sets:
```bash
  bash run_refiner.sh
```

#### (1) [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06)

```bash
  python refiner.py \
    --model-name Llama-3-ELYZA-JP-8B
  
  python run.py \
    --model-name Llama-3-ELYZA-JP-8B \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Llama-3-ELYZA-JP-8B/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Llama-3-ELYZA-JP-8B/output_refiner_synth \
    --out_csv refiner/Llama-3-ELYZA-JP-8B/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (2) [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) (Release: 2025/03)

```bash
  python refiner.py \
    --model-name Llama-3-Karamaru-v1
  
  python run.py \
    --model-name Llama-3-Karamaru-v1 \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Llama-3-Karamaru-v1/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Llama-3-Karamaru-v1/output_refiner_synth \
    --out_csv refiner/Llama-3-Karamaru-v1/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (3) [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07)

```bash
  python refiner.py \
    --model-name Llama-3-Youko-8B-Instruct
  
  python run.py \
    --model-name Llama-3-Youko-8B-Instruct \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Llama-3-Youko-8B-Instruct/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Llama-3-Youko-8B-Instruct/output_refiner_synth \
    --out_csv refiner/Llama-3-Youko-8B-Instruct/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (4) [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12)

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
    --out_csv refiner/Llama-3.1-Swallow-8B-Instruct-v0.3/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (5) [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03)

```bash
  python refiner.py \
    --model-name RakutenAI-7B-Instruct
  
  python run.py \
    --model-name RakutenAI-7B-Instruct \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/RakutenAI-7B-Instruct/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/RakutenAI-7B-Instruct/output_refiner_synth \
    --out_csv refiner/RakutenAI-7B-Instruct/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (6) [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05)

```bash
  python refiner.py \
    --model-name Gemma-2-Llama-Swallow-9b-it-v0.1
  
  python run.py \
    --model-name Gemma-2-Llama-Swallow-9b-it-v0.1 \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Gemma-2-Llama-Swallow-9b-it-v0.1/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Gemma-2-Llama-Swallow-9b-it-v0.1/output_refiner_synth \
    --out_csv refiner/Gemma-2-Llama-Swallow-9b-it-v0.1/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (7) [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02)

```bash
  python refiner.py \
    --model-name Qwen3-Swallow-8B-RL-v0.2
  
  python run.py \
    --model-name Qwen3-Swallow-8B-RL-v0.2 \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/Qwen3-Swallow-8B-RL-v0.2/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/Qwen3-Swallow-8B-RL-v0.2/output_refiner_synth \
    --out_csv refiner/Qwen3-Swallow-8B-RL-v0.2/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```

#### (8) [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04)

```bash
  python refiner.py \
    --model-name LLM-jp-4-8B-Instruct
  
  python run.py \
    --model-name LLM-jp-4-8B-Instruct \
    --input-dir dataset/test/synthetic/input \
    --output-dir refiner/LLM-jp-4-8B-Instruct/output_refiner_synth
  
  python evaluate.py \
    --gt_dir dataset/test/synthetic/gt \
    --pred_dir refiner/LLM-jp-4-8B-Instruct/output_refiner_synth \
    --out_csv refiner/LLM-jp-4-8B-Instruct/output_refiner_synth_cer.csv \
    --baseline_dir dataset/test/synthetic/input
```
