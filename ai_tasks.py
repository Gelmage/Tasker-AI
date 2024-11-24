from openai_utils import ask_openai
from system_tasks import run_workflow
import subprocess

def execute_ai_task(command):
    """Execute an AI task by delegating it to the workflow manager."""
    return run_workflow(command)




