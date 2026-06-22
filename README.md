# KCR-Post-Processing
### 1. [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06/26)
#### Download
```
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./Llama-3-ELYZA-JP-8B/model
```
#### Run
```
  python ./Llama-3-ELYZA-JP-8B/run.py
```
#### Evaluate
```
  python ./Llama-3-ELYZA-JP-8B/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Llama-3-ELYZA-JP-8B/output --out_csv ./Llama-3-ELYZA-JP-8B/output_csv
```

### 2. [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07/25)
#### Download
```
  hf download rinna/llama-3-youko-8b-instruct --local-dir ./Llama-3-Youko-8B-Instruct/model
```
#### Run
```
  python ./Llama-3-Youko-8B-Instruct/run.py
```
#### Evaluate
```
  python ./Llama-3-Youko-8B-Instruct/evaluate.py --gt_dir ./dataset/gt --pred_dir ./Llama-3-Youko-8B-Instruct/output --out_csv ./Llama-3-Youko-8B-Instruct/output_csv
```

### 3. [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12/23)
#### Download
```
  hf download tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3 --local-dir ./Llama-3.1-Swallow-8B-Instruct-v0.3/model
```
#### Run
```
  python ./Llama-3.1-Swallow-8B-Instruct-v0.3/run.py
```
#### Evaluate
```
  python ./Llama-3.1-Swallow-8B-Instruct-v0.3/evaluate.py --gt_dir ./dataset/gt --pred_dir ./output --out_csv ./Llama-3.1-Swallow-8B-Instruct-v0.3/output_csv
```

### 4. [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) (Release: 2024/03/21)
#### Download
```
  cd ./RakutenAI-7B-Instruct
  hf download Rakuten/RakutenAI-7B-instruct --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 5. [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) (Release: 2025/05/19)
#### Download
```
  cd ./Gemma-2-Llama-Swallow-9b-it-v0.1
  hf download tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1 --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 6. [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02/20)
#### Download
```
  cd ./Qwen3-Swallow-8B-RL-v0.2
  hf download tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2 --local-dir ./model
```
#### Run
```
  python ./run.py
```

#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 7. [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) (Release: 2026/04/03)
#### Download
```
  cd ./LLM-jp-4-8B-Instruct
  hf download llm-jp/llm-jp-4-8b-instruct --local-dir ./model
```
#### Run
```
  python ./run.py
```

#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```
