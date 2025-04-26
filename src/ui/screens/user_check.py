from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class UserCheckScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        self.title = QLabel("Welcome to Banking App")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)
        
        # Buttons
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.parent.switch_to_login)
        layout.addWidget(self.login_button)
        
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.parent.switch_to_signup)
        layout.addWidget(self.signup_button)
        
        self.setLayout(layout)
        
        # Apply styles
        with open("src/styles/user_check.qss", "r") as f:
            self.setStyleSheet(f.read())