# gui.py

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit,
    QTextEdit, QPushButton, QWidget
)
from ai_logic import handle_user_input  # Import the function from ai_logic.py

class AIAgentGUI(QMainWindow):
    def __init__(self, ai_logic_callback):
        super().__init__()

        # Save the callback function to communicate with AI logic
        self.ai_logic_callback = ai_logic_callback

        # Set up the main window
        self.setWindowTitle("AI Agent")
        self.setGeometry(100, 100, 600, 400)

        # Set up the layout and widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.input_field = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)

        self.layout.addWidget(self.output_area)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.submit_button)

        self.submit_button.clicked.connect(self.handle_submit)
        self.input_field.returnPressed.connect(self.handle_submit)  # Handle Enter key

        # Initial greeting
        self.output_area.append("AI: Hello! I'm your AI Agent. How can I assist you?")

    def handle_submit(self):
        """Handle user input and display AI response."""
        user_input = self.input_field.text().strip()
        if not user_input:
            return  # Ignore empty input
        if user_input.lower() in ["exit", "quit"]:
            self.close()
        else:
            response = self.ai_logic_callback(user_input)
            self.output_area.append(f"You: {user_input}")
            self.output_area.append(f"AI: {response}")
            self.output_area.append("")  # Add a blank line for readability
            self.input_field.clear()
            # Scroll to the bottom
            self.output_area.verticalScrollBar().setValue(
                self.output_area.verticalScrollBar().maximum()
            )

    def closeEvent(self, event):
        """Handle the event when the window is closed."""
        self.output_area.append("AI: Goodbye!")
        event.accept()
