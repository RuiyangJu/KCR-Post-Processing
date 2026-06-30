## Zero-shot LLM Post-processing
### Result
| Model | Affiliation | Release Date | Base | Checkpoint Size | Latency@Real (sec) | CER@Real (%) | Latency@Syn. (sec) | CER@Syn. (%) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [Baseline](https://github.com/RuiyangJu/Seal-Robust-KCR) | / | / | / | / | / | 11.98 | / | 13.68 |
| [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) | 株式会社ELYZA | 2024.06 | Meta-Llama-3-8B-Instruct | 16.1GB | 2.305 | 13.72 (9.70%) | 2.329 | 15.19 (10.96%) |
| [Llama-3-Karamaru-v1](https://huggingface.co/SakanaAI/Llama-3-Karamaru-v1) | SakanaAI | 2025.03 | Llama-3-ELYZA-JP-8B | 16.1GB | 3.612 | 71.14 (10.22%) | 3.802 | 75.16 (11.31%) |
| [Llama-3-Youko-8B-Instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct) | rinna株式会社 | 2024.07 | Meta-Llama-3-8B | 16.1GB | 2.342 | 25.98 (13.37%) | 2.350 | 28.23 (14.61%) |
| [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) | 東京科学大学 | 2024.12 | Meta-Llama-3.1-8B-Instruct | 16.1GB | 2.345 | 12.26 (8.74%) | 2.361 | 13.93 (10.00%) |
| [RakutenAI-7B-Instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) | 楽天グループ株式会社 | 2024.03 | Mistral-7B-v0.1 | 29.5GB | 2.142 | 20.65 (10.10%) | 2.026 | 18.07 (11.08%) |
| [Gemma-2-Llama-Swallow-9b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-it-v0.1) | 東京科学大学 | 2025.05 | Gemma-2-9B | 18.5GB | 3.427 | 20.08 (9.51%) | 3.434 | 21.23 (10.69%) |
| [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) | 東京科学大学 | 2026.02 | Qwen3-8B | 16.4GB | 2.578 | 12.28 (9.01%) | 2.599 | 14.12 (10.21%) |
| [LLM-jp-4-8B-Instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) | 国立情報学研究所 | 2026.04 | Llama 2 architecture | 17.2GB | 1.902 | 13.88 (8.81%) | 1.875 | 15.31 (10.01%) |

* The values in parentheses are the results obtained after removing abnormal pages with a CER greater than 25%.
