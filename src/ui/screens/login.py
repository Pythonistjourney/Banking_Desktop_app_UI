from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer
from src.services.api import APIClient
from src.utils.validators import UserLoginSchema

class LoginScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_client = APIClient()
        self.animations = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(40)

        # Animated bank name
        bank_name = "AUT Finance Bank"
        header_container = QWidget()
        header_layout = QHBoxLayout(header_container)
        header_layout.setAlignment(Qt.AlignCenter)
        header_layout.setSpacing(6)

        for char in bank_name:
            label = QLabel(char)
            label.setObjectName("title")
            label.setProperty("opacity", 0.0)
            header_layout.addWidget(label)

            # Animation for each character
            anim = QPropertyAnimation(label, b"opacity")
            anim.setDuration(500)
            anim.setStartValue(0.0)
            anim.setEndValue(1.0)
            self.animations.append(anim)

        main_layout.addWidget(header_container)

        # Card container
        card = QWidget()
        card.setObjectName("card")
        card.setFixedWidth(450)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("Sign in to continue")
        title.setObjectName("subtitle")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        card_layout.addWidget(self.username_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        card_layout.addWidget(self.password_input)

        # Terms checkbox
        terms_layout = QHBoxLayout()
        terms_checkbox = QCheckBox("I agree with the terms and conditions")
        terms_layout.addWidget(terms_checkbox)
        card_layout.addLayout(terms_layout)

        # Error message
        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        # Login button
        login_button = QPushButton("Log In")
        login_button.clicked.connect(self.handle_login)
        card_layout.addWidget(login_button)

        # Links
        links_layout = QHBoxLayout()
        signup_link = QPushButton("Don't have an account? Sign Up")
        signup_link.setObjectName("link")
        signup_link.clicked.connect(lambda: self.parent().switch_screen('Signup'))
        links_layout.addWidget(signup_link)
        card_layout.addLayout(links_layout)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

        # Start header animation
        self.start_animations()

    def start_animations(self):
        for i, anim in enumerate(self.animations):
            QTimer.singleShot(i * 100, lambda: anim.start())

    def handle_login(self):
        try:
            login_data = {
                'login_id': self.username_input.text(),
                'Password': self.password_input.text(),
            }
            UserLoginSchema.validate(login_data)
            response = self.api_client.post('/api/v1/users/login', login_data)
            if response.get('success'):
                self.parent().switch_screen('Dashboard')
            else:
                self.error_label.setText(response.get('message', 'Login failed'))
        except Exception as e:
            self.error_label.setText(str(e))

    def opacity(self, widget, value):
        widget.setStyleSheet(f"opacity: {value};")