# KCR-Post-Processing
## Zero-shot LLM Post-processing
### Overview


### 1. [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06/26)
#### Download & Run & Evaluate
```
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./Llama-3-ELYZA-JP-8B/model
  python ./Llama-3-ELYZA-JP-8B/run.py
  python ./Llama-3-ELYZA-JP-8B/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Llama-3-ELYZA-JP-8B/output --out_csv ./Llama-3-ELYZA-JP-8B/output_csv
```

### 2. [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07/25)
#### Download & Run & Evaluate
```
  hf download rinna/llama-3-youko-8b-instruct --local-dir ./Llama-3-Youko-8B-Instruct/model
  python ./Llama-3-Youko-8B-Instruct/run.py
  python ./Llama-3-Youko-8B-Instruct/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Llama-3-Youko-8B-Instruct/output --out_csv ./Llama-3-Youko-8B-Instruct/output_csv
```

### 3. [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12/23)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3 --local-dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/model
  python ./Llama-3.1-Swallow-8B-Instruct-v0.3/run.py
  python ./Llama-3.1-Swallow-8B-Instruct-v0.3/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/output --out_csv ./Llama-3.1-Swallow-8B-Instruct-v0.3/output_csv
```

### 4. [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03/21)
#### Download & Run & Evaluate
```
  hf download Rakuten/RakutenAI-7B-instruct --local-dir ./RakutenAI-7B-Instruct/model
  python ./RakutenAI-7B-Instruct/run.py
  python ./RakutenAI-7B-Instruct/evaluate.py --gt_dir ./dataset/gt --pred_dir ./RakutenAI-7B-Instruct/output --out_csv ./RakutenAI-7B-Instruct/output_csv
```

### 5. [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05/19)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1 --local-dir ./Gemma-2-Llama-Swallow-9b-it-v0.1/model
  python ./Gemma-2-Llama-Swallow-9b-it-v0.1/run.py
  python ./Gemma-2-Llama-Swallow-9b-it-v0.1/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Gemma-2-Llama-Swallow-9b-it-v0.1/output --out_csv ./Gemma-2-Llama-Swallow-9b-it-v0.1/output_csv
```

### 6. [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02/20)
#### Download & Run & Evaluate
```
  hf download tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2 --local-dir ./Qwen3-Swallow-8B-RL-v0.2/model
  python ./Qwen3-Swallow-8B-RL-v0.2/run.py
  python ./Qwen3-Swallow-8B-RL-v0.2/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Qwen3-Swallow-8B-RL-v0.2/output --out_csv ./Qwen3-Swallow-8B-RL-v0.2/output_csv
```

### 7. [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04/03)
#### Download & Run & Evaluate
```
  hf download llm-jp/llm-jp-4-8b-instruct --local-dir ./LLM-jp-4-8B-Instruct/model
  python ./LLM-jp-4-8B-Instruct/run.py
  python ./LLM-jp-4-8B-Instruct/evaluate.py --gt_dir ./dataset/gt --pred_dir ./LLM-jp-4-8B-Instruct/output --out_csv ./LLM-jp-4-8B-Instruct/output_csv
```

## Base-LLM Refiner
