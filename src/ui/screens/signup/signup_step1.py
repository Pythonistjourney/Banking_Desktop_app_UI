from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Signal

class SignupStep1(QWidget):
    next_step = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)  # Create and set the main layout
        self.setup_ui()

    def setup_ui(self):
        # Basic info fields
        self.username_input = self.create_input_field("Username:")
        self.email_input = self.create_input_field("Email:")
        self.password_input = self.create_input_field("Password:", is_password=True)
        self.confirm_password_input = self.create_input_field("Confirm Password:", is_password=True)

        # Next button
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.handle_next)

        self.main_layout.addStretch()
        self.main_layout.addWidget(next_button)

    def create_input_field(self, label_text, is_password=False):
        container = QWidget()
        layout = QHBoxLayout(container)
        
        label = QLabel(label_text)
        input_field = QLineEdit()
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
            
        layout.addWidget(label)
        layout.addWidget(input_field)
        
        self.main_layout.addWidget(container)
        return input_field

    def handle_next(self):
        data = {
            "username": self.username_input.text(),
            "email": self.email_input.text(),
            "password": self.password_input.text(),
            "confirm_password": self.confirm_password_input.text()
        }
        self.next_step.emit(data)