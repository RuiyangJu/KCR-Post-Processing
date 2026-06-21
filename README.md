# KCR-Post-Processing

## [elyza/Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B)
### Download Model
```
  cd ./Llama-3-ELYZA-JP-8B
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./model
```
### Run
```
  python ./run.py
```
### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```

## [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2)
### Download Model
```
  cd ./Qwen3-Swallow-8B-RL-v0.2
  hf download tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2 --local-dir ./model
```
### Run
```
  python ./run.py
```

### Evaluate
```
  python ./evaluate.py --gt_dir ../dataset/gt --pred_dir ./output --out_csv ./output_csv
```
