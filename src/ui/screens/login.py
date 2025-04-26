from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt, QPropertyAnimation
from src.api.client import APIClient
from src.schemas.schemas import UserLogin
from src.context.user_context import UserContext

class LoginScreen(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.api_client = APIClient()
        self.user_context = UserContext()
        self.animations = []
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(40)

        bank_name = QLabel("AUT Finance Bank")
        bank_name.setObjectName("bank_name")
        bank_name.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(bank_name)

        tagline = QLabel("Secure Banking Solutions")
        tagline.setObjectName("tagline")
        tagline.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(tagline)

        card = QWidget()
        card.setObjectName("card")
        card.setFixedWidth(450)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Sign in to your account")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username or email")
        card_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)  # Fixed: Changed from lowercase 'password' to 'Password'
        card_layout.addWidget(self.password_input)

        terms_layout = QHBoxLayout()
        terms_checkbox = QCheckBox(" Agree to terms and conditions")
        terms_layout.addWidget(terms_checkbox)
        card_layout.addLayout(terms_layout)

        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        login_button = QPushButton("Log In")
        login_button.clicked.connect(self.handle_login)
        card_layout.addWidget(login_button)

        links_layout = QHBoxLayout()
        signup_link = QPushButton("Don't have an account? Sign Up")
        signup_link.setObjectName("link")
        signup_link.clicked.connect(lambda: self.navigation_manager.switch_screen('Signup'))
        links_layout.addWidget(signup_link)
        card_layout.addLayout(links_layout)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

        self.start_animation(title)

    def start_animation(self, widget):
        anim = QPropertyAnimation(widget, b"windowOpacity")
        anim.setDuration(800)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.start()

    def handle_login(self):
        if not self.username_input.text() or not self.password_input.text():
            self.error_label.setText("Please fill in all fields")
            return
        

        try:
            login_data = UserLogin(
                username = self.username_input.text(),
                password = self.password_input.text()
            )
            response = self.api_client.login(login_data)
            self.user_context.set_user(response.dict(), response.access_token)
            self.error_label.setText("Login successful!")
            self.navigation_manager.switch_screen('Dashboard')
        except Exception as e:
            if "connection" in str(e).lower():
                self.error_label.setText("Cannot connect to server. Please make sure the backend service is running.")
            else:
                self.error_label.setText(f"Login failed: {str(e)}")