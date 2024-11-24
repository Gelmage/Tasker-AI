import subprocess
import pyautogui
import time
import json
import os
import re
import logging
from openai_utils import ask_openai

def open_program(program_name):
    try:
        command = program_commands.get(program_name.lower())
        if command:
            subprocess.Popen(command)
            return f"Opened {program_name}."
        else:
            return f"Program '{program_name}' not recognized."
    except Exception as e:
        return f"Failed to open program: {e}"
    
def write_to_program(text):
    try:
        time.sleep(2)  # Wait for the program to open
        pyautogui.write(text, interval=0.05)
        return f"Typed: {text}"
    except Exception as e:
        return f"Error writing to program: {e}"

def focus_window(window_title):
    try:
        if os.name == 'posix':
            result = subprocess.run(["wmctrl", "-a", window_title], capture_output=True, text=True)
            if result.returncode == 0:
                return f"Focused on window: {window_title}."
            else:
                return f"Window '{window_title}' not found."
        else:
            return "Focus window action is not supported on this platform."
    except Exception as e:
        return f"Error focusing on window: {e}"
    
def extract_json(text):
    json_pattern = re.compile(r'\[.*\]', re.DOTALL)
    match = json_pattern.search(text)
    if match:
        return match.group()
    else:
        return None

def parse_command_to_tasks(command):
    prompt = f"""
    You are an assistant that translates natural language commands into executable tasks.
    Break the following user command into a list of tasks.
    Each task should be a JSON object with an 'action' key and any required parameters.
    Provide the list of tasks as a JSON array.

    Example:
    [
        {{"action": "open_program", "program": "notepad"}},
        {{"action": "write_to_program", "content": "Hello, world!"}}
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
            return [{"action": "error", "message": f"Failed to parse JSON: {e}\nJSON Content: {json_content}"}]
    else:
        return [{"action": "error", "message": f"No JSON found in response.\nResponse: {response}"}]

def execute_task(task):
    action = task.get("action")
    if action == "open_program":
        return open_program(task.get("program"))
    elif action == "focus_window":
        return focus_window(task.get("window_title"))
    elif action == "write_to_program":
        return write_to_program(task.get("content"))
    else:
        return f"Unknown action: {action}"

def run_workflow(command):
    tasks = parse_command_to_tasks(command)
    logging.debug(f"Parsed tasks - {tasks}")
    results = []
    for task in tasks:
        result = execute_task(task)
        results.append(result)
    return "\n".join(results)
            