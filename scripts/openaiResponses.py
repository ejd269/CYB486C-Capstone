import json
from openai import OpenAI

client = OpenAI(api_key="[Insert API key here]")

def classify_emails(file):
    with open(file, "r", encoding="utf-8") as file:
        emails = json.load(file)

    for email in emails:
       prompt = f"""
       Classify each email as Malicious or Safe. Return the label and a brief explanation.

       Email:
       email_id: {email["email_id"]}
       timestamp: {email["timestamp"]}
       sender: {email["sender"]}
       subject: {email["subject"]}
       body: {email["body"]}
"""
      
       response = client.responses.create(
          model="gpt-4o-mini",
          input=prompt)
       
       print(f"Email ID: {email['email_id']}")
       print(f"Email Classification: {email['classification']}")
       print(f"")
       print(f"OpenAI Response: {response.output_text}")
       print("-" * 200)


classify_emails("datasets/[Insert test file here]")
