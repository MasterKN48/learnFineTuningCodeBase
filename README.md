# Learn Fine-Tuning with Gemma-3 and Unsloth-MLX

This project is set up for local fine-tuning of the **Gemma-3 270m** model on Apple Silicon using the [unsloth-mlx](https://github.com/unslothai/unsloth-mlx) library.

## Prerequisites

- **Apple Silicon Mac**: M1, M2, M3, M4, or M5.
- **Unified RAM**: 16GB minimum (32GB+ recommended for larger models).
- **UV**: Fast Python package manager.

## Setup

1. **Install Dependencies**:
   ```bash
   uv sync
   ```
   (This installs `mlx`, `unsloth-mlx`, `datasets`, and `jupyter`).

2. **Model Placement**:
   Place your Gemma-3 270m model files in a directory named `gemma3` at the root of the project. This directory is ignored by git.

3. **Environment**:
   The `.env` file contains:
   ```env
   MLX_MODEL_PATH=./gemma3
   ```
   Modify this if your model is located elsewhere.

## Local Fine-Tuning

Open the provided Jupyter Notebook to start the fine-tuning process:

```bash
uv run jupyter notebook finetune.ipynb
```

The notebook is pre-configured to:
- Load the model from the path in `.env`.
- Apply LoRA adapters.
- Provide a template for dataset preparation and training.

## Note on Gemma-3 270m
Gemma-3 270m is a highly efficient small language model, making it ideal for local fine-tuning on Mac devices without requiring high-performance cloud GPUs.
