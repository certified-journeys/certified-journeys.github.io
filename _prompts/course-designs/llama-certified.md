# Course Design: Llama & Local LLMs in Production

## Metadata

```
COURSE_ID:        llama-certified
COURSE_FULL_NAME: Llama & Local LLMs in Production
ICON:             LL
ACCENT_COLOR:     #0057FF
ACCENT_LIGHT:     #E6EEFF
ACCENT_DARK:      #003FCC
ACCENT_DARK_DIM:  #000F33
PROVIDER:         Meta / Ollama (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Advanced
TAGS:             LLMs, Llama, Ollama, Python, Inference
EXAM_LINK:        https://llama.meta.com/docs/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Fine-tune a Llama model on a domain dataset and serve it via an OpenAI-compatible API as the capstone.
CAPSTONE_PROJECT: Fine-tune Llama-3.2-1B with QLoRA on a domain-specific dataset (customer support or medical QA), convert the merged adapter to GGUF, load it into Ollama with a custom Modelfile, serve it via the OpenAI-compatible REST API, and benchmark it against the base model on 20 held-out prompts measuring accuracy and tokens/sec.
```

## AI Deep Dive Topics (3 cards)

1. **GGUF quantization internals** — how Q4_K_M packs 4-bit weights into 64-element blocks with per-block scale factors (K-quants), why K-quants (K_S, K_M, K_L) outperform legacy Q4_0 at the same bit-width by preserving more information in the scaling metadata, and when Q8_0 is worth the 2x memory cost over Q4_K_M (accuracy-sensitive tasks, coding, math).

2. **QLoRA memory math** — how 4-bit NF4 quantization of the base model plus LoRA adapter training in bfloat16 lets a 7B model fine-tune in under 10GB VRAM, why `r=16 alpha=32` is the safe starting LoRA config for most tasks, and why paged AdamW is critical for avoiding OOM spikes during gradient accumulation on long sequences.

3. **OpenAI-compatible serving** — how Ollama's `/v1/chat/completions` endpoint is wire-compatible with the OpenAI Python SDK (swap `base_url` and `api_key="ollama"`), what the latency difference is between Ollama's single-process server and vLLM's PagedAttention-based continuous batching, and when to switch: Ollama for dev/single-user, vLLM for multi-user prod serving.

## Notebooks

```
NOTEBOOKS:
  day-01-llama-model-family
  day-02-ollama-local-setup
  day-03-quantization-gguf
  day-04-inference-backends
  day-05-prompt-formatting
  day-06-qlora-finetuning
  day-07-gguf-conversion
  day-08-ollama-rest-api
  day-09-benchmarking
  day-10-capstone-domain-model
```

## Days

### Day 1 — Llama Model Family: Variants, Parameters, and Context Windows
**Badge:** learn

### Day 2 — Running Llama Locally with Ollama
**Badge:** learn

### Day 3 — Quantization: GGUF Formats and Quality vs Speed Tradeoffs
**Badge:** practice

### Day 4 — Inference Backends: llama.cpp, vLLM, and Transformers
**Badge:** practice

### Day 5 — Prompt Formatting: Chat Templates and Instruction Formatting
**Badge:** practice

### Day 6 — Fine-Tuning with QLoRA on Consumer Hardware
**Badge:** practice

### Day 7 — GGUF Conversion and Custom Modelfiles
**Badge:** practice

### Day 8 — Serving with Ollama REST API and OpenAI-Compatible Endpoints
**Badge:** practice

### Day 9 — Benchmarking: Tokens/sec, Memory, and Quality Metrics
**Badge:** review

### Day 10 — Capstone: Fine-Tune and Serve a Domain-Specific Llama Model
**Badge:** exam
