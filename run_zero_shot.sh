#!/usr/bin/env bash
set -e

MODELS=(
  "Llama-3-ELYZA-JP-8B"
  "Llama-3-Karamaru-v1"
  "Llama-3-Youko-8B-Instruct"
  "Llama-3.1-Swallow-8B-Instruct-v0.3"
  "RakutenAI-7B-Instruct"
  "Gemma-2-Llama-Swallow-9b-it-v0.1"
  "Qwen3-Swallow-8B-RL-v0.2"
  "LLM-jp-4-8B-Instruct"
)

SETS=(
  "synthetic synth"
  "real real"
)

for MODEL in "${MODELS[@]}"; do
  for ITEM in "${SETS[@]}"; do
    read -r DATASET SUFFIX <<< "$ITEM"

    INPUT_DIR="dataset/test/${DATASET}/input"
    GT_DIR="dataset/test/${DATASET}/gt"
    OUTPUT_DIR="zero_shot/${MODEL}/output_base_${SUFFIX}"
    OUT_CSV="zero_shot/${MODEL}/output_base_${SUFFIX}_cer.csv"

    echo "=========================================="
    echo "Running model: ${MODEL}"
    echo "Dataset: ${DATASET}"
    echo "Output: ${OUTPUT_DIR}"
    echo "=========================================="

    python run.py \
      --model-name "${MODEL}" \
      --no-adapter \
      --input-dir "${INPUT_DIR}" \
      --output-dir "${OUTPUT_DIR}"

    python evaluate.py \
      --gt_dir "${GT_DIR}" \
      --pred_dir "${OUTPUT_DIR}" \
      --out_csv "${OUT_CSV}"

    echo "Finished: ${MODEL} on ${DATASET}"
    echo
  done
done

echo "All zero-shot runs and evaluations finished."
