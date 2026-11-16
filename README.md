# local-llm-model
Play around local model


# Local machines setup

## Hardware

| Component | Details |
|-----------|---------|
| CPU | Intel Core i9-14900KS (24 cores / 32 threads) |
| GPU | NVIDIA GeForce RTX 5090 (32 GB VRAM, driver 591.86) |
| iGPU | Intel UHD Graphics 770 |
| RAM | 96 GB |
| Motherboard | Gigabyte Z790 A PRO X WIFI7 |

## Storage

| Drive | Size | Free | Notes |
|-------|------|------|-------|
| C: | 931 GB | 711 GB | System |
| D: | 2.7 TB | 1.6 TB | |
| E: | 3.7 TB | 3.7 TB | Ollama models (`E:\OllamaModels`) |
| F: | 7.4 TB | 7.4 TB | |

## Software

- **OS**: Windows 11 Pro (build 26200), 64-bit
- **Ollama**: v0.40.16, installed at `%LOCALAPPDATA%\Programs\Ollama`
  - `OLLAMA_MODELS` is set to `E:\OllamaModels` (user environment variable)
- **Python**: 3.14.5
- **Node.js**: v24.16.0

## Installed models

| Model | Size |
|-------|------|
| qwen3:14b | 9.3 GB |
