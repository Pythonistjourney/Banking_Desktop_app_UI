from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from src.services.user_service import getUserDetails

class DashboardScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(40)

        # Header
        header = QLabel("Welcome to AUT Finance Bank")
        header.setObjectName("title")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        # Balance card
        balance_card = QWidget()
        balance_card.setObjectName("dashboard_card")
        balance_layout = QVBoxLayout(balance_card)
        balance_layout.setSpacing(10)

        balance_title = QLabel("Account Balance")
        balance_title.setObjectName("subtitle")
        balance_layout.addWidget(balance_title)

        self.balance_label = QLabel("Loading...")
        self.balance_label.setStyleSheet("font-size: 24px; color: #FFFFFF; font-family: 'Roboto';")
        balance_layout.addWidget(self.balance_label)

        main_layout.addWidget(balance_card)

        # Services grid
        services_card = QWidget()
        services_card.setObjectName("dashboard_card")
        services_layout = QGridLayout(services_card)
        services_layout.setSpacing(20)

        services = ["Send Money", "Deposit", "Withdraw", "Cards", "Transactions", "Loan"]
        for i, service in enumerate(services):
            btn = QPushButton(service)
            services_layout.addWidget(btn, i // 3, i % 3)

        main_layout.addWidget(services_card)
        main_layout.addStretch()
        self.setLayout(main_layout)

        # Fetch user data
        self.fetch_user_data()

    def fetch_user_data(self):
        try:
            user_data = getUserDetails()
            self.balance_label.setText(f"${user_data.get('Balance', 0):.2f}")
        except Exception as e:
            self.balance_label.setText("Error loading balance")