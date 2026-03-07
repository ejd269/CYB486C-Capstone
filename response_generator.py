# Be sure to install the OpenAI package in your system terminal
# Command is "pip install openai" for Windows

from openai import OpenAI

client = OpenAI(api_key="[Insert key here]")

ticket = ["Say hello", "Say goodbye"]

def generate_response(input):
  for item in input:
    response = client.responses.create(
      model="gpt-4.1-mini",
      input=item)
   
    print(response.output_text)

generate_response(ticket)
