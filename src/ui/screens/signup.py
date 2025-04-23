from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt
from src.services.api import APIClient
from src.utils.validators import UserCreateSchema

class SignupStep1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_client = APIClient()
        self.signup_data = {}
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(40)

        # Bank name and tagline
        bank_name = QLabel("AUT Finance Bank")
        bank_name.setObjectName("bank_name")
        bank_name.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(bank_name)

        tagline = QLabel("Secure Banking Solutions")
        tagline.setObjectName("tagline")
        tagline.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(tagline)

        # Card container
        card = QWidget()
        card.setObjectName("card")
        card.setFixedWidth(450)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(40, 40, 40, 40)

        # Title
        title = QLabel("Create your account")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("To manage your finances with ease")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitle)

        # Progress dots
        dots_layout = QHBoxLayout()
        dots_layout.setAlignment(Qt.AlignCenter)
        for i in range(6):
            dot = QLabel()
            dot.setFixedSize(12, 12)
            dot.setObjectName("dot_active" if i == 0 else "dot")
            dots_layout.addWidget(dot)
        card_layout.addLayout(dots_layout)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setText("webmail@mail.com")
        card_layout.addWidget(self.username_input)

        # Full name input
        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Enter your full name")
        card_layout.addWidget(self.fullname_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Create a password")
        self.password_input.setEchoMode(QLineEdit.Password)
        card_layout.addWidget(self.password_input)

        # Terms checkbox
        terms_layout = QHBoxLayout()
        terms_checkbox = QCheckBox("Agree to terms and conditions")
        terms_layout.addWidget(terms_checkbox)
        card_layout.addLayout(terms_layout)

        # Status message
        status_message = QLabel("Download our mobile app for better experience")
        status_message.setStyleSheet("font-size: 14px; color: #FFFFFF; font-family: 'Roboto';")
        status_message.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(status_message)

        # Error message
        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        # Signup button
        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        card_layout.addWidget(signup_button)

        # Back to login link
        login_link = QPushButton("Already have an account? Login")
        login_link.setObjectName("link")
        login_link.clicked.connect(lambda: self.parent().switch_screen('Login'))
        card_layout.addWidget(login_link)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def handle_signup(self):
        try:
            self.signup_data = {
                'Username': self.username_input.text(),
                'FullName': self.fullname_input.text(),
                'Password': self.password_input.text(),
            }
            UserCreateSchema.validate(self.signup_data, partial=True)
            self.error_label.setText("Proceed to next step (not implemented)")
        except Exception as e:
            self.error_label.setText(str(e))