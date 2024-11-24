import logging
from ai_tasks import execute_ai_task

def handle_user_input(command):
    """Handle user input and return AI response."""
    return execute_ai_task(command)


def parse_command_to_tasks(command):
    """Parse a natural language command into actionable tasks using OpenAI."""
    prompt = f"""
You are an assistant that translates natural language commands into executable tasks.
Break the following user command into a list of tasks.
Each task should be a JSON object with an 'action' key and any required parameters.
Only use the following actions: "open_program", "write_to_program", "focus_window", "output_text".
Provide the list of tasks as a JSON array.

Example:
[
    {{"action": "open_program", "program": "notepad"}},
    {{"action": "write_to_program", "content": "Hello, world!"}},
    {{"action": "output_text", "content": "Task completed successfully."}}
]

Now, parse the user's command and provide the tasks in JSON format only.

User command: "{command}"
"""
    response = ask_openai(prompt)
    response = response.strip()
    json_content = extract_json(response)
    if json_content:
        try:
            tasks = json.loads(json_content)
            return tasks
        except Exception as e:
            logging.error(f"Failed to parse JSON: {e}\nJSON Content: {json_content}")
            return [{"action": "error", "message": f"Failed to parse JSON: {e}"}]
    else:
        logging.error(f"No JSON found in response.\nResponse: {response}")
        return [{"action": "error", "message": "No JSON found in response."}]

def execute_task(task):
    """Execute a single task based on its action."""
    action = task.get("action")
    if action == "open_program":
        return open_program(task.get("program"))
    elif action == "focus_window":
        return focus_window(task.get("window_title"))
    elif action == "write_to_program":
        return write_to_program(task.get("content"))
    elif action == "output_text":
        # Return the 'content' or 'text' field from the task
        return task.get("content") or task.get("text") or "No content provided."
    elif action == "error":
        return task.get("message")
    else:
        return f"Unknown action: {action}"






from system_tasks import (
    open_program,
    write_to_program,
    focus_window,
    output_text,
    extract_json,
    run_workflow
)
def execute_ai_task(command):
    """Execute an AI task by delegating it to the workflow manager."""
    return run_workflow(command)

# ai_logic.py

from system_tasks import run_workflow

def execute_ai_task(command):
    """Execute an AI task by delegating it to the workflow manager."""
    return run_workflow(command)


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'

def parse_command_to_tasks(command, retries=3):
    """Parse a natural language command into actionable tasks using OpenAI."""
    prompt = f"""
    You are an assistant that translates natural language commands into executable tasks.
    Break the following user command into a list of tasks.
    Each task should be a JSON object with an 'action' key and any required parameters.
    Only use the following actions: "open_program", "write_to_program", "focus_window", "output_text".
    Provide the list of tasks as a JSON array without any additional text or explanations.
    Enclose the JSON in ```json ... ``` code blocks.

    Example:
    ```json
    [
        {{"action": "open_program", "program": "notepad"}},
        {{"action": "write_to_program", "content": "Hello, world!"}},
        {{"action": "output_text", "content": "Task completed successfully."}}
    ]
    ```
    Now, parse the user's command and provide the tasks in JSON format only.

    User command: "{command}"
    """
    for attempt in range(1, retries + 1):
        response = ask_openai(prompt)
        logging.debug(f"Raw OpenAI response (Attempt {attempt}): {response}")
        response = response.strip()

        # Remove code block markers if present
        if response.startswith('```json') and response.endswith('```'):
            response = response[7:-3].strip()

        json_content = extract_json(response)
        if json_content:
            try:
                tasks = json.loads(json_content)
                logging.debug(f"Parsed tasks: {tasks}")
                return tasks
            except json.JSONDecodeError as e:
                logging.error(f"JSON parsing error on attempt {attempt}: {e}")
        else:
            logging.error(f"No JSON found in response on attempt {attempt}.")

    # After retries, return an error
    logging.error("Failed to parse command after multiple attempts.")
    return [{"action": "error", "message": "Failed to parse command after multiple attempts."}]

def execute_task(task):
    """Execute a single task based on its action."""
    action = task.get("action")
    if not action:
        logging.warning("No action specified in task.")
        return "No action specified."

    if action == "open_program":
        program = task.get("program")
        if not program:
            logging.warning("No program specified to open.")
            return "No program specified to open."
        return open_program(program)
    elif action == "focus_window":
        window_title = task.get("window_title")
        if not window_title:
            logging.warning("No window title specified to focus.")
            return "No window title specified to focus."
        return focus_window(window_title)
    elif action == "write_to_program":
        content = task.get("content")
        if not content:
            logging.warning("No content specified to write.")
            return "No content specified to write."
        return write_to_program(content)
    elif action == "output_text":
        content = task.get("content")
        if not content:
            logging.warning("No content specified for output_text.")
            return "No content specified for output_text."
        logging.info(f"Output text: {content}")
        return content
    elif action == "error":
        message = task.get("message", "An unknown error occurred.")
        logging.error(f"AI Error: {message}")
        return message
    else:
        logging.warning(f"Unknown action received: {action}")
        return f"Unknown action: {action}"

def run_workflow(command):
    """Parse and execute tasks from a natural language command."""
    tasks = parse_command_to_tasks(command)
    results = []
    for task in tasks:
        result = execute_task(task)
        results.append(result)
    return "\n".join(results)

