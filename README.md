# KCR-Post-Processing
## 🦙 Llama
### ① [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B)
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

### ② [Llama-3-Youko-8B](https://huggingface.co/rinna/llama-3-youko-8b)
#### Download
```
  cd ./Llama-3-Youko-8B
  hf download rinna/llama-3-youko-8b --local-dir ./model
```
#### Run
```
  python ./run.py
```
#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

### ③ [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)
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

## 🔍 Qwen
### ① [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2)
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

### ② [Nekomata-7B-Instruction](https://huggingface.co/rinna/nekomata-7b-instruction)
#### Download
```
  cd ./Nekomata-7B-Instruction
  hf download rinna/nekomata-7b-instruction --local-dir ./model
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
