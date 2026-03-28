import json
from openai import OpenAI

# API key for responses API
client = OpenAI(api_key="[insert API key here]")

# Model used by responses API
modelName = "[insert model name here]"

# Opens testingData for input into model
with open("datasets/testingData.json", "r", encoding="utf-8") as file:
    testData = json.load(file)

# Retrieves labels from answerSheet for comparison with model output
with open("datasets/answerSheet.json", "r", encoding="utf-8") as file:
    answerSheet = json.load(file)
labels = [entry["label"] for entry in answerSheet]

labelValue = 0
counter = 1

print(f"Model Name: {modelName}")
print(f"")
print("-" * 50)
print(f"")

for testEmail in testData:
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
    From: {testEmail["spoofed_sender"]}
    Subject: {testEmail["subject"]}
    Body: {testEmail["body"]}
"""
    
    response = client.responses.create(
        model=modelName,
        input=prompt)
    
    print(f"Email #{counter}")
    counter += 1
    print(f"Subject: {testEmail['subject']}")
    print(f"Expected Label: {labels[labelValue]}")
    labelValue += 1
    print(f"")
    print(f"{response.output_text}")
    print(f"")
    print("-" * 50)
    print(f"")

print(f"CLASSIFICATION COMPLETE")
print(f"")
