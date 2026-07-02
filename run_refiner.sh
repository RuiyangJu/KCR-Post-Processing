#!/usr/bin/env bash
set -euo pipefail

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
  REFINER_DIR="refiner/${MODEL}"
  REFINER_MODEL_DIR="refiner/${MODEL}/model"
  LOG_FILE="${REFINER_DIR}/logs.txt"

  mkdir -p "${REFINER_DIR}"

  {
  echo "=========================================="
  echo "Log file: ${LOG_FILE}"
  echo "Started at: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "=========================================="

  echo "=========================================="
  echo "Training refiner: ${MODEL}"
  echo "Adapter output: ${REFINER_MODEL_DIR}"
  echo "=========================================="

  python refiner.py \
    --model-name "${MODEL}" \
    --output-dir "${REFINER_MODEL_DIR}"

  for ITEM in "${SETS[@]}"; do
    read -r DATASET SUFFIX <<< "$ITEM"

    INPUT_DIR="dataset/test/${DATASET}/input"
    GT_DIR="dataset/test/${DATASET}/gt"
    OUTPUT_DIR="refiner/${MODEL}/output_refiner_${SUFFIX}"
    OUT_CSV="refiner/${MODEL}/output_refiner_${SUFFIX}_cer.csv"

    echo "=========================================="
    echo "Running refiner model: ${MODEL}"
    echo "Dataset: ${DATASET}"
    echo "Output: ${OUTPUT_DIR}"
    echo "=========================================="

    python run.py \
      --model-name "${MODEL}" \
      --adapter-dir "${REFINER_MODEL_DIR}" \
      --input-dir "${INPUT_DIR}" \
      --output-dir "${OUTPUT_DIR}"

    python evaluate.py \
      --gt_dir "${GT_DIR}" \
      --pred_dir "${OUTPUT_DIR}" \
      --out_csv "${OUT_CSV}" \
      --baseline_dir "${INPUT_DIR}"

    echo "Finished refiner evaluation: ${MODEL} on ${DATASET}"
    echo
  done

  echo "=========================================="
  echo "Finished model: ${MODEL}"
  echo "Finished at: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "=========================================="
  } 2>&1 | tee "${LOG_FILE}"
done

echo "All refiner training, runs, and evaluations finished."
