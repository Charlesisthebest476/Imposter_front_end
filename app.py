import json
import os
import google
from google import genai


client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a joke about robots"
)

print(response.txt)