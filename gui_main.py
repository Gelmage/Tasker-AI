# gui_main.py

import sys
from PyQt5.QtWidgets import QApplication
from gui import AIAgentGUI
from ai_logic import execute_ai_task

def main():
    """Main function to run the AI Agent with GUI."""
    app = QApplication(sys.argv)
    window = AIAgentGUI(ai_logic_callback=execute_ai_task)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
