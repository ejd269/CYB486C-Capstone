import json
from openai import OpenAI

client = OpenAI(api_key="[Insert API key here]")

# Creates a dataset for fine-tuning
dataset = client.files.create(
    file = open("datasets/finetuneData.jsonl", "rb"),
    purpose = "fine-tune",
    expires_after = {
        "anchor": "created_at",
        "seconds": 2592000
    }
)

# Initiates a fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file = dataset.id,
    model="gpt-4.1-2025-04-14"
)

print(f"Model ID:     {job.id}")
print(f"Status:       {job.status}")
print(f"")
