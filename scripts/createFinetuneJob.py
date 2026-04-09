import json
from openai import OpenAI

client = OpenAI(api_key="[Insert API key here]")

# Creates a dataset for fine-tuning
dataset = client.files.create(
    file = open("[Insert training data file path here]", "rb"),
    purpose = "fine-tune",
    expires_after = {
        "anchor": "created_at",
        "seconds": 2592000
    }
)

# Initiates a fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file = dataset.id,
    model="[Insert model name here]",
    suffix="[Insert suffix here]"
)

print(f"Model ID:     {job.id}")
print(f"Status:       {job.status}")
print(f"")
