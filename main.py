# At the top of your scripts
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# main.py

import logging
from ai_logic import execute_ai_task

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """Main function to interact with the AI Agent via CLI."""
    print("Hello! I'm your AI Agent. How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.strip() == '':
            continue  # Ignore empty input
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        else:
            response = execute_ai_task(user_input)
            print(f"AI: {response}")

if __name__ == "__main__":
    main()
