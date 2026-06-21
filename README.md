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

## 🌸 LLM-jp
### ① [LLM-jp-4-8B-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking)
#### Download
```
  cd ./llm-jp-4-8b-thinking
  hf download llm-jp/llm-jp-4-8b-thinking --local-dir ./model
```
#### Run
```
  python ./run.py
```

#### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```


