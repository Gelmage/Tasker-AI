# At the top of your scripts
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# openai_utils.py

import openai
import os

# Set the OpenAI API key from an environment variable

def ask_openai(prompt):
    """Send a prompt to OpenAI and return its response."""
    try:
        response = openai.chat.completions.create(model="gpt-4",
        messages=[
            # System prompt can be adjusted as needed
            {"role": "system", "content": "You are an assistant that translates natural language commands into executable tasks."},
            {"role": "user", "content": prompt},
        ])
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"
