## Zero-shot LLM Post-processing
### Run & Evaluate: Synthetic Test Set Example
#### Root
```
  cd KCR-Post-Processing 
```
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
