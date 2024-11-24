# At the top of your scripts
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ai_logic.py

from system_tasks import run_workflow

def execute_ai_task(command):
    """Execute an AI task by delegating it to the workflow manager."""
    return run_workflow(command)
