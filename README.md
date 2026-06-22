# KCR-Post-Processing
### 1. [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) (Release: 2024/06/26)
#### Download
```
  cd ./Llama-3-ELYZA-JP-8B
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 2. [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) (Release: 2024/07/25)
#### Download
```
  cd ./Llama-3-Youko-8B-Instruct
  hf download rinna/llama-3-youko-8b-instruct --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 3. [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) (Release: 2024/12/23)
#### Download
```
  cd ./Llama-3.1-Swallow-8B-Instruct-v0.3
  hf download tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3 --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### 4. [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) (Release: 2026/02/20)
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

## 🌸 LLM-jp
### ① [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct)
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

## 💎 Gemma
