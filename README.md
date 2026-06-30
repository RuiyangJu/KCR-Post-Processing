# KCR Post-Processing

### Environment
* OS: Linux
* GPU: NVIDIA RTX PRO 6000 Blackwell
* CPU: Intel Core i5-12600K

### Parameter
| Parameter | Setting |
|:--:|:--:|
| `max_new_tokens` | `1024` |
| `do_sample` | `False` |
| `temperature` | `None` |
| `top_p` | `None` |
| `num_beams` | `1` |
| `repetition_penalty` | `1.0` |
| `torch_dtype` | `auto` |
| `device_map` | `{"": "cuda:0"}` |
| `attn_implementation` | `sdpa` |
| `add_special_tokens` | `False` |
| `add_generation_prompt` | `True` |

### Prompt
All models use the same OCR correction instruction:
```
  あなたは日本古典籍OCRの誤り訂正システムです。
  
  OCRによる明らかな誤字・脱字・衍字だけを、原文の文脈に基づいて訂正してください。
  歴史的仮名遣い、旧字体、異体字、漢文調の表現は現代語に変更しないでください。
  根拠のない補完、要約、説明、注釈を加えず、原文の内容と順序を維持してください。
  修正後の本文のみを出力してください。
```

### Download Pre-trained Models
```
  cd KCR-Post-Processing
  hf download elyza/Llama-3-ELYZA-JP-8B --local-dir ./model/Llama-3-ELYZA-JP-8B
```
### 1. Zero-shot LLM Post-processing
* Japanese LLM Leaderboard [here](https://swallow-llm.github.io/leaderboard).
* 
### 2. LLM-based OCR Refiner Fine-tuning
