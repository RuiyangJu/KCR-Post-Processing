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
* We evaluate several Japanese-specific LLMs in a zero-shot OCR post-processing setting.
* The model selection is based in part on the [Japanese LLM Leaderboard](https://swallow-llm.github.io/leaderboard).

### Results

| Model | Affiliation | Release Date | Base Model | Checkpoint Size | Latency@Real (sec) | CER@Real (%) | Latency@Syn. (sec) | CER@Syn. (%) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [Baseline](https://github.com/RuiyangJu/Seal-Robust-KCR) | – | – | – | – | – | 11.98 | – | 13.67 |
| [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) | ELYZA, Inc. | 2024.06 | Meta-Llama-3-8B-Instruct | 16.1 GB | 2.305 | 13.71 (9.69) | 2.329 | 15.19 (10.96) |
| [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) | Sakana AI | 2025.03 | Llama-3-ELYZA-JP-8B | 16.1 GB | 3.612 | 72.04 (10.20) | 3.802 | 75.16 (11.31) |
| [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) | rinna Co., Ltd. | 2024.07 | Meta-Llama-3-8B | 16.1 GB | 2.342 | 26.77 (13.37) | 2.350 | 28.23 (14.61) |
| [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) | Institute of Science Tokyo | 2024.12 | Meta-Llama-3.1-8B-Instruct | 16.1 GB | 2.345 | 12.25 (8.73) | 2.361 | 13.93 (10.00) |
| [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) | Rakuten Group, Inc. | 2024.03 | Mistral-7B-v0.1 | 29.5 GB | 2.142 | 20.64 (10.10) | 2.026 | 18.07 (11.08) |
| [Gemma-2-Llama-Swallow-9B-IT-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) | Institute of Science Tokyo | 2025.05 | Gemma-2-9B | 18.5 GB | 3.427 | 20.07 (9.51) | 3.434 | 21.23 (10.69) |
| [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) | Institute of Science Tokyo | 2026.02 | Qwen3-8B | 16.4 GB | 2.578 | 12.27 (9.01) | 2.599 | 14.12 (10.21) |
| [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) | National Institute of Informatics | 2026.04 | Llama 2 architecture | 17.2 GB | 1.902 | 16.24 (8.81) | 1.875 | 17.82 (10.01) |

* The values in parentheses indicate CER results after removing outlier pages with a CER greater than 25%.
* Implementation commands are provided in [zero_shot/](zero_shot/), with detailed error analyses available in each model-specific folder.

## 2. LLM-based OCR Refiner Fine-tuning
