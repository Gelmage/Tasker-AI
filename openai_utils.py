import openai
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Set the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

def ask_openai(prompt):
    """Send a prompt to OpenAI and return its response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that translates natural language commands into executable tasks."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,      # Adjust creativity
            max_tokens=150,       # Adjust based on expected response length
            n=1,
            stop=None
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logging.error(f"Error communicating with OpenAI: {e}")
        return f"Error communicating with OpenAI: {e}"
