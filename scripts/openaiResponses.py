import json
from openai import OpenAI

#API key for responses API
client = OpenAI(api_key="[insert API key here]")

# Model used by responses API
modelName = "[insert model name here]"

# Classifies emails using OpenAI API with file provided below
def classify_emails(file):
    with open(file, "r", encoding="utf-8") as file:
        emails = json.load(file)

    counter = 1

    print(f"Model Name: {modelName}")
    print(f"")

    for email in emails:
       prompt = f"""
       You are an email security classifier. 
       For each email, return the result in the following format:
       
       Label: <phishing or benign>
       Intent: <intent>
       Technique: <technique>
       Target: <target>
       
       Return exactly in this format with no extra text.

       Here is the following email to classify:
       
       Email:
       From: {email["spoofed_sender"]}
       Subject: {email["subject"]}
       Body: {email["body"]}
"""
       
       response = client.responses.create(
          model=modelName,
          input=prompt)
       
       print(f"Email #{counter}")
       counter += 1
       print(f"Subject: {email['subject']}")
       print(f"{response.output_text}")
       print(f"")
       print("-" * 100)
       print(f"")

    print(f"CLASSIFICATION COMPLETE")
    print(f"")

classify_emails("datasets/testingData.json")
