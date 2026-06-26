## Zero-shot LLM Post-processing
### Environment
* OS: Linux
* GPU: NVIDIA RTX PRO 6000 Blackwell
* CPU: Intel Core i5-12600K

### Parameter
| Parameter | Setting |
|:--:|:--:|
| `max_new_tokens` | `1024` |
| `do_sample` | `False` |
| `temperature` | `None` |
| `top_p` | `None` |
| `num_beams` | `1` |
| `repetition_penalty` | `1.0` |
| `batch_size` | `1` |
| `torch_dtype` | `auto` |
| `device` | `cuda:0` |
| `device_map` | `{"": "cuda:0"}` |
| `attention implementation` | `sdpa` |
| `add_special_tokens` | `False` |
| `add_generation_prompt` | `True` |

### Prompt
All models use the same OCR correction instruction:
```
  あなたは日本古典籍OCRの誤り訂正システムです。
  
  OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
  歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
  根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
  修正後の本文のみを出力してください。
```

### Result
| Model | Affiliation | Release Date | Base | Model Size | Latency@Real (sec) | CER@Real (%) | Latency@Syn. (sec) | CER@Syn. (%) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [Baseline](https://github.com/RuiyangJu/Seal-Robust-KCR) | / | / | / | / | / | 11.98 | / | 13.68 |
| [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) | 株式会社ELYZA | 2024.06.26 | Meta-Llama-3-8B-Instruct | 16.1GB | 2.305 | 13.72 (9.70%) | 2.329 | 15.19 (10.96%) |
| [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) | SakanaAI | 2025.03.31 | Llama-3-ELYZA-JP-8B | 16.1GB | 3.612 | 71.14 (10.22%) | 3.802 | 75.16 (11.31%) |
| [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) | rinna株式会社 | 2024.07.25 | Meta-Llama-3-8B | 16.1GB | 2.342 | 25.98 (13.37%) | 2.350 | 28.23 (14.61%) |
| [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) | 東京科学大学 | 2024.12.23 | Meta-Llama-3.1-8B-Instruct | 16.1GB | 2.345 | 12.26 (8.74%) | 2.361 | 13.93 (10.00%) |
| [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) | 楽天グループ株式会社 | 2024.03.21 | Mistral-7B-v0.1 | 29.5GB | 2.142 | 20.65 | 2.026 | 18.07 |
| [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) | 東京科学大学 | 2025.05.19 | Gemma-2-9B | 18.5GB | 3.427 | 20.08 | 3.434 | 21.23 |
| [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) | 東京科学大学 | 2026.02.20 | Qwen3-8B | 16.4GB | 2.578 | 12.28 | 2.599 | 14.12 |
| [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) | 國立情報學研究所 | 2026.04.03 | Llama 2 architecture | 17.2GB | 1.902 | 13.88 | 1.875 | 15.31 |

### Root
```
  cd zero_shot
```

### (1) [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06/26)
#### Download & Run & Evaluate
```
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./Llama-3-ELYZA-JP-8B/model
  python ./Llama-3-ELYZA-JP-8B/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Llama-3-ELYZA-JP-8B/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Llama-3-ELYZA-JP-8B/output_synthetic --out_csv ./Llama-3-ELYZA-JP-8B/output_syn_csv
```

### (2) [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) (Release: 2025/03/31)
#### Download & Run & Evaluate
```
  hf download SakanaAI/Llama-3-Karamaru-v1 --local-dir ./Llama-3-Karamaru-v1/model
  python ./Llama-3-Karamaru-v1/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Llama-3-Karamaru-v1/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Llama-3-Karamaru-v1/output_synthetic --out_csv ./Llama-3-Karamaru-v1/output_syn_csv
```

### (3) [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07/25)
#### Download & Run & Evaluate
```
  hf download rinna/llama-3-youko-8b-instruct --local-dir ./Llama-3-Youko-8B-Instruct/model
  python ./Llama-3-Youko-8B-Instruct/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Llama-3-Youko-8B-Instruct/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Llama-3-Youko-8B-Instruct/output_synthetic --out_csv ./Llama-3-Youko-8B-Instruct/output_syn_csv
```

### (4) [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12/23)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3 --local-dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/model
  python ./Llama-3.1-Swallow-8B-Instruct-v0.3/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/output_synthetic --out_csv ./Llama-3.1-Swallow-8B-Instruct-v0.3/output_syn_csv
```

### (5) [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03/21)
#### Download & Run & Evaluate
```
  hf download Rakuten/RakutenAI-7B-instruct --local-dir ./RakutenAI-7B-Instruct/model
  python ./RakutenAI-7B-Instruct/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./RakutenAI-7B-Instruct/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./RakutenAI-7B-Instruct/output_synthetic --out_csv ./RakutenAI-7B-Instruct/output_syn_csv
```

### (6) [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05/19)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1 --local-dir ./Gemma-2-Llama-Swallow-9b-it-v0.1/model
  python ./Gemma-2-Llama-Swallow-9b-it-v0.1/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Gemma-2-Llama-Swallow-9b-it-v0.1/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Gemma-2-Llama-Swallow-9b-it-v0.1/output_synthetic --out_csv ./Gemma-2-Llama-Swallow-9b-it-v0.1/output_syn_csv
```

### (7) [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02/20)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2 --local-dir ./Qwen3-Swallow-8B-RL-v0.2/model
  python ./Qwen3-Swallow-8B-RL-v0.2/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./Qwen3-Swallow-8B-RL-v0.2/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./Qwen3-Swallow-8B-RL-v0.2/output_synthetic --out_csv ./Qwen3-Swallow-8B-RL-v0.2/output_syn_csv
```

### (8) [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04/03)
#### Download & Run & Evaluate
```
  hf download llm-jp/llm-jp-4-8b-instruct --local-dir ./LLM-jp-4-8B-Instruct/model
  python ./LLM-jp-4-8B-Instruct/run.py --input-dir ../dataset/synthetic/input/ --output-dir ./LLM-jp-4-8B-Instruct/output_synthetic
  python ./evaluate.py --gt_dir ../dataset/synthetic/gt --pred_dir ./LLM-jp-4-8B-Instruct/output_synthetic --out_csv ./LLM-jp-4-8B-Instruct/output_syn_csv
```
