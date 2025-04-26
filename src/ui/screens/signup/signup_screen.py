from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox,
    QFormLayout
)
from PySide6.QtCore import Qt

class SignupScreen(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Title
        title = QLabel("Sign Up")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Form layout for inputs
        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        # Username field
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        form_layout.addRow("Username:", self.username_input)

        # Password field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("Password:", self.password_input)

        # Confirm password field
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("Confirm Password:", self.confirm_password_input)

        main_layout.addLayout(form_layout)

        # Sign Up button
        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        main_layout.addWidget(signup_button)

        # Login link
        login_link = QPushButton("Already have an account? Login")
        login_link.setFlat(True)
        login_link.clicked.connect(self.go_to_login)
        main_layout.addWidget(login_link)

    def handle_signup(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "passwords do not match")
            return

        # TODO: Implement actual signup logic here
        QMessageBox.information(self, "Success", "Account created successfully!")
        self.go_to_login()

    def go_to_login(self):
        self.navigation_manager.switch_screen('Login')  # Changed from navigate_to_login to switch_screeny