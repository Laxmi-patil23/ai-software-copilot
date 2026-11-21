import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Get API key safely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Code Explanation Feature

print("\n===== AI SOFTWARE ENGINEERING COPILOT =====")

print("\nEnter your Python code.")
print("Type END on a new line when finished:\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

user_code = "\n".join(lines)

prompt = f"""
You are an expert Python programming assistant.

Explain the following Python code:
1. Explain the purpose of the code.
2. Explain it line by line.
3. Explain important functions and variables.
4. Show the expected output.

Code:
{user_code}
"""

# Send code to Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

# Display AI response
print("\n===== CODE EXPLANATION =====")
print(response.text)
