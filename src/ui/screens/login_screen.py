from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer
from src.services.api import APIClient
from src.utils.validators import UserLoginSchema

class LoginScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_client = APIClient()
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

        # Welcome message with fade-in animation
        welcome_message = QLabel("Welcome back...")
        welcome_message.setObjectName("welcome_message")
        welcome_message.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(welcome_message)

        # Card container
        card = QWidget()
        card.setObjectName("card")
        card.setFixedWidth(450)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(40, 40, 40, 40)

        # Title
        title = QLabel("Sign in to your account")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("To access your banking dashboard")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitle)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setText("webmail@mail.com")
        card_layout.addWidget(self.username_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        card_layout.addWidget(self.password_input)

        # Terms checkbox
        terms_layout = QHBoxLayout()
        terms_checkbox = QCheckBox("Login with terms and conditions")
        terms_layout.addWidget(terms_checkbox)
        card_layout.addLayout(terms_layout)

        # Error message
        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        # Login button
        login_button = QPushButton("Continue to my account")
        login_button.clicked.connect(self.handle_login)
        card_layout.addWidget(login_button)

        # Links
        links_layout = QHBoxLayout()
        forgot_password_link = QPushButton("Forgot password?")
        forgot_password_link.setObjectName("link")
        forgot_password_link.clicked.connect(lambda: self.parent().switch_screen('ForgotPassword'))
        links_layout.addWidget(forgot_password_link)

        signup_link = QPushButton("Don't have an account? Sign Up")
        signup_link.setObjectName("link")
        signup_link.clicked.connect(lambda: self.parent().switch_screen('Signup'))
        links_layout.addWidget(signup_link)

        card_layout.addLayout(links_layout)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

        # Start animation
        self.start_animation(welcome_message)

    def start_animation(self, widget):
        anim = QPropertyAnimation(widget, b"windowOpacity")
        anim.setDuration(800)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.start()

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