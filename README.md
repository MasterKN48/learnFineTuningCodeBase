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

   (This installs `mlx`, `unsloth-mlx`, `datasets`, `jupyter`, `tensorboard`, and `trl`).

2. **Model Placement**:
   Place your Gemma-3 270m model files in a directory named `gemma3` at the root of the project. This directory is ignored by git.

3. **Environment Configuration**:
   The `.env` file manages your paths:
   ```env
   MLX_MODEL_PATH=./gemma3
   DATASET_PATH=dataset.jsonl
   ```

## Dataset Preparation

To train the model on your own code, you first need to convert your files into a format the training script can understand.

1. **Generate Dataset**:
   Run the following script to crawl the `codebase/` directory and create your training file:

   ```bash
   python prepare_dataset.py
   ```

   This extracts `.html`, `.css`, and `.js` files and pairs them with instructions like "Write the code for the file index.html".

2. **Output**:
   The script generates a file named `dataset.jsonl` (or whatever path you set in `.env`).

### What is JSONL Format?

**JSONL (JSON Lines)** is a text format where each line is a valid JSON object. It is the standard format for LLM training data because:

- **Streaming**: Large datasets can be read line-by-line without loading the entire file into memory.
- **Robustness**: If one line is corrupted, the rest of the file remains readable.
- **Structure**: Each line typically represents one training example.

**Example of our `dataset.jsonl`:**

```json
{"instruction": "Write the code for index.html", "input": "", "output": "<html>...</html>"}
{"instruction": "Explain the logic in script.js", "input": "", "output": "console.log('hello');"}
```

## Local Fine-Tuning

Open the provided Jupyter Notebook to start the fine-tuning process:

```bash
uv run jupyter notebook finetune.ipynb
```

The notebook is pre-configured to:

- Resolve paths from your `.env` file.
- Load the model using **QLoRA** (4-bit quantization).
- Configure training via **`SFTConfig`** for organized management of hyperparameters.
- Run the actual training loop via `trainer.train()`.

## Monitoring Progress

Visualizing your training progress is crucial for understanding how well the model is learning.

- **TensorBoard**: The notebook is integrated with TensorBoard. It logs training loss and other metrics to the `./lora_finetuned` directory. You can launch it directly inside the notebook to see real-time graphs.
- **Interactive Progress Bars**: Thanks to `ipywidgets`, you'll see clean, interactive progress bars directly in the notebook cells while `trainer.train()` is running.

## Saving and Persistence

When training finishes, the notebook saves your **LoRA adapters** to the `lora_model/` directory.

- **Non-Destructive**: This does NOT modify your original `gemma3` model files.
- **Portability**: You only need to share the `lora_model/` folder to use your fine-tuned version on other Macs.

## Testing the Model

After training, you can verify the results in **Step 5** of the notebook.

1. **Switch to Inference**: The notebook uses `FastLanguageModel.for_inference(model)` which optimizes the model for generation.
2. **Generate response**: Enter a prompt like "Write the code for index.html" to see how well the model has learned your codebase.

## Note on Gemma-3 270m

Gemma-3 270m is a highly efficient small language model, making it ideal for local fine-tuning on Mac devices without requiring high-performance cloud GPUs.
