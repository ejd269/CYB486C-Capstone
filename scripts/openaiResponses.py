import json
from openai import OpenAI

client = OpenAI(api_key="[Insert API key here]")

# Classifies emails using OpenAI API with file provided below
def classify_emails(file):
    with open(file, "r", encoding="utf-8") as file:
        emails = json.load(file)

    counter = 1

    for email in emails:
       prompt = f"""
       Classify each email as Phishing or Benign. Return the label and a brief explanation.

       Email:
       From: {email["spoofed_sender"]}
       Subject: {email["subject"]}
       Body: {email["body"]}
"""
       
       response = client.responses.create(
          model="gpt-4o-mini",
          input=prompt)
       
       print(f"Email #{counter}")
       counter += 1
       print(f"Subject: {email['subject']}")
       print(f"OpenAI Response: {response.output_text}")
       print(f"")
       print("-" * 200)
       print(f"")

    print(f"Classification Complete")

classify_emails("datasets/testingData.json")
