import psutil
import logging
from ai_logic import handle_user_input  # Import the function from ai_logic.py

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def speak(text):
    """Simulate speaking by printing the text."""
    print(f"Speaking: {text}")

def system_health():
    """Check system health."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return f"CPU Usage: {cpu}%, Memory Usage: {memory}%, Disk Usage: {disk}%."

def main():
    """Main function to interact with the AI Agent via CLI."""
    greeting = "Hello! I'm your AI Agent. How can I assist you?"
    print(greeting)
    speak(greeting)

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            speak("Goodbye!")
            break

        if user_input.strip() == '':
            continue  # Ignore empty input

        if user_input.lower() in ["exit", "quit"]:
            farewell = "Goodbye!"
            print(farewell)
            speak(farewell)
            break
        elif user_input.lower() == "system health":
            health = system_health()
            print(health)
            speak(health)
        else:
            response = handle_user_input(user_input)  # Use handle_user_input from ai_logic.py
            print(f"AI: {response}")
            speak(response)

if __name__ == "__main__":
    main()
