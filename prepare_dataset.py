import os
import json
from dotenv import load_dotenv

load_dotenv()


def prepare_dataset(base_dir="codebase", output_file=None):
    if output_file is None:
        output_file = os.getenv("DATASET_PATH", "dataset.jsonl")

    dataset = []

    # Supported file extensions
    supported_extensions = {".html", ".css", ".js"}

    print(f"Crawling directory: {base_dir}")

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in supported_extensions:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_dir)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Create instruction-output pairs
                    # We can create multiple variants of instructions for each file
                    instructions = [
                        f"Write the code for the file `{rel_path}` in the codebase project.",
                        f"What is the content of `{rel_path}`?",
                        f"Implement the `{rel_path}` file for the web project.",
                    ]

                    for instr in instructions:
                        dataset.append(
                            {"instruction": instr, "input": "", "output": content}
                        )

                    print(f"  Processed: {rel_path}")
                except Exception as e:
                    print(f"  Error processing {rel_path}: {e}")

    print(f"Writing {len(dataset)} entries to {output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in dataset:
            f.write(json.dumps(entry) + "\n")


if __name__ == "__main__":
    prepare_dataset()
