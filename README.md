# KCR Post-Processing
## Environment
* OS: Linux
* GPU: NVIDIA RTX PRO 6000 Blackwell
* CPU: Intel Core i5-12600K

## Inference Parameters
| Parameter | Setting |
|:--:|:--:|
| `max_new_tokens` | `1024` |
| `do_sample` | `False` |
| `temperature` | `None` |
| `top_p` | `None` |
| `num_beams` | `1` |
| `repetition_penalty` | `1.0` |
| `torch_dtype` | `auto` |
| `device_map` | `{"": "cuda:0"}` |
| `attn_implementation` | `sdpa` |
| `add_special_tokens` | `False` |
| `add_generation_prompt` | `True` |

## Prompt
All models use the same OCR correction instruction:
```
あなたは日本古典籍OCRの誤り訂正システムです。

OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
修正後の本文のみを出力してください。
```

## Download Base Models
Run the following commands to download the base LLMs from Hugging Face:
```
  cd KCR-Post-Processing
  
  hf download elyza/Llama-3-ELYZA-JP-8B \
    --local-dir ./model/Llama-3-ELYZA-JP-8B
  
  hf download SakanaAI/Llama-3-Karamaru-v1 \
    --local-dir ./model/Llama-3-Karamaru-v1
  
  hf download rinna/llama-3-youko-8b-instruct \
    --local-dir ./model/Llama-3-Youko-8B-Instruct
  
  hf download tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3 \
    --local-dir ./model/Llama-3.1-Swallow-8B-Instruct-v0.3
  
  hf download Rakuten/RakutenAI-7B-instruct \
    --local-dir ./model/RakutenAI-7B-Instruct
  
  hf download tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1 \
    --local-dir ./model/Gemma-2-Llama-Swallow-9b-it-v0.1
  
  hf download tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2 \
    --local-dir ./model/Qwen3-Swallow-8B-RL-v0.2
  
  hf download llm-jp/llm-jp-4-8b-instruct \
    --local-dir ./model/LLM-jp-4-8B-Instruct
```
## 1. Zero-shot LLM Post-processing
Detailed result tables and error analysis are provided in [zero_shot/](zero_shot/).

### Run & Evaluate: Synthetic Test Set Example
#### (1) [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06)

```bash
python run.py \
  --model-name Llama-3-ELYZA-JP-8B \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Llama-3-ELYZA-JP-8B/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Llama-3-ELYZA-JP-8B/output_base_synth \
  --out_csv zero_shot/Llama-3-ELYZA-JP-8B/output_base_synth_cer.csv
```

#### (2) [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) (Release: 2025/03)

```bash
python run.py \
  --model-name Llama-3-Karamaru-v1 \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Llama-3-Karamaru-v1/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Llama-3-Karamaru-v1/output_base_synth \
  --out_csv zero_shot/Llama-3-Karamaru-v1/output_base_synth_cer.csv
```

#### (3) [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07)

```bash
python run.py \
  --model-name Llama-3-Youko-8B-Instruct \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Llama-3-Youko-8B-Instruct/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Llama-3-Youko-8B-Instruct/output_base_synth \
  --out_csv zero_shot/Llama-3-Youko-8B-Instruct/output_base_synth_cer.csv
```

#### (4) [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12)

```bash
python run.py \
  --model-name Llama-3.1-Swallow-8B-Instruct-v0.3 \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Llama-3.1-Swallow-8B-Instruct-v0.3/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Llama-3.1-Swallow-8B-Instruct-v0.3/output_base_synth \
  --out_csv zero_shot/Llama-3.1-Swallow-8B-Instruct-v0.3/output_base_synth_cer.csv
```

#### (5) [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03)

```bash
python run.py \
  --model-name RakutenAI-7B-Instruct \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/RakutenAI-7B-Instruct/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/RakutenAI-7B-Instruct/output_base_synth \
  --out_csv zero_shot/RakutenAI-7B-Instruct/output_base_synth_cer.csv
```

#### (6) [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05)

```bash
python run.py \
  --model-name Gemma-2-Llama-Swallow-9b-it-v0.1 \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/output_base_synth \
  --out_csv zero_shot/Gemma-2-Llama-Swallow-9b-it-v0.1/output_base_synth_cer.csv
```

#### (7) [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02)

```bash
python run.py \
  --model-name Qwen3-Swallow-8B-RL-v0.2 \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/Qwen3-Swallow-8B-RL-v0.2/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/Qwen3-Swallow-8B-RL-v0.2/output_base_synth \
  --out_csv zero_shot/Qwen3-Swallow-8B-RL-v0.2/output_base_synth_cer.csv
```

#### (8) [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04)

```bash
python run.py \
  --model-name LLM-jp-4-8B-Instruct \
  --no-adapter \
  --input-dir dataset/test/synthetic/input \
  --output-dir zero_shot/LLM-jp-4-8B-Instruct/output_base_synth

python evaluate.py \
  --gt_dir dataset/test/synthetic/gt \
  --pred_dir zero_shot/LLM-jp-4-8B-Instruct/output_base_synth \
  --out_csv zero_shot/LLM-jp-4-8B-Instruct/output_base_synth_cer.csv
```

## 2. LLM-based OCR Refiner Fine-tuning
