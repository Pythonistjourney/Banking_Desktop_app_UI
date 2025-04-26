from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox, QDateEdit
from PySide6.QtCore import Qt, QDate
from src.api.client import APIClient
from src.schemas.schemas import UserCreate
from src.context.user_context import UserContext
from datetime import date

class SignupScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_client = APIClient()
        self.user_context = UserContext()
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

        title = QLabel("Create your account")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        card_layout.addWidget(self.username_input)

        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Enter your full name")
        card_layout.addWidget(self.fullname_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        card_layout.addWidget(self.email_input)

        self.cnic_input = QLineEdit()
        self.cnic_input.setPlaceholderText("Enter CNIC (xxxxx-xxxxxxx-x)")
        card_layout.addWidget(self.cnic_input)

        self.dob_input = QDateEdit()
        self.dob_input.setDisplayFormat("yyyy-MM-dd")
        self.dob_input.setDate(QDate(1990, 1, 1))
        card_layout.addWidget(self.dob_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Create a password")
        self.password_input.setEchoMode(QLineEdit.password)
        card_layout.addWidget(self.password_input)

        terms_layout = QHBoxLayout()
        terms_checkbox = QCheckBox(" Agree to terms and conditions")
        terms_layout.addWidget(terms_checkbox)
        card_layout.addLayout(terms_layout)

        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        card_layout.addWidget(signup_button)

        login_link = QPushButton("Already have an account? Login")
        login_link.setObjectName("link")
        login_link.clicked.connect(lambda: self.parent().switch_screen('Login'))
        card_layout.addWidget(login_link)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def handle_signup(self):
        if not all([self.username_input.text(), self.fullname_input.text(), self.email_input.text(), 
                    self.cnic_input.text(), self.password_input.text()]):
            self.error_label.setText("Please fill in all fields")
            return

        try:
            signup_data = UserCreate(
                username=self.username_input.text(),
                FirstName=self.fullname_input.text().split()[0] if self.fullname_input.text() else "",
                LastName=" ".join(self.fullname_input.text().split()[1:]) if len(self.fullname_input.text().split()) > 1 else "",
                Email=self.email_input.text(),
                CNIC=self.cnic_input.text(),
                DateOfBirth=date(self.dob_input.date().year(), self.dob_input.date().month(), self.dob_input.date().day()),
                password=self.password_input.text(),
                AccountType="Savings",
                IsActive=False,
            )
            response = self.api_client.register(signup_data)
            self.user_context.set_user(response.dict(), None)
            self.error_label.setText("Registration successful!")
            self.parent().switch_screen('Dashboard')
        except Exception as e:
            self.error_label.setText(f"Registration failed: {str(e)}")