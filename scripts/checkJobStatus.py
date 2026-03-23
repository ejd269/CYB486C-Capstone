from openai import OpenAI

client = OpenAI(api_key="[Insert API key here]")

# List all job details
jobs = client.fine_tuning.jobs.list()

for job in jobs.data:
    print(job.id, job.fine_tuned_model,job.status)

print(f"")

# # Uses job.id from list() to get details for a specific job
# job = client.fine_tuning.jobs.retrieve("[insert job id here]")

# print(f"Job ID:     {job.id}")
# print(f"Job Status: {job.status}")
# print(f"Job Name:   {job.fine_tuned_model}")
# print(f"")
