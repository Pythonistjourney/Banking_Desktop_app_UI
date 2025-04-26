from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PySide6.QtCore import Qt
from src.api.client import APIClient
from src.context.user_context import UserContext

class DashboardScreen(QWidget):
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

        balance_card = QWidget()
        balance_card.setObjectName("dashboard_card")
        balance_layout = QVBoxLayout(balance_card)
        balance_layout.setSpacing(10)

        balance_title = QLabel("Account Overview")
        balance_title.setObjectName("title")
        balance_layout.addWidget(balance_title)

        self.balance_label = QLabel("Loading balance...")
        self.balance_label.setObjectName("balance")
        balance_layout.addWidget(self.balance_label)

        self.analytics_label = QLabel("Loading analytics...")
        self.analytics_label.setObjectName("balance")
        balance_layout.addWidget(self.analytics_label)

        main_layout.addWidget(balance_card)

        services_card = QWidget()
        services_card.setObjectName("dashboard_card")
        services_layout = QGridLayout(services_card)
        services_layout.setSpacing(20)

        services = ["Send Money", "Deposit", "Withdraw", "Cards", "Transactions", "Loan"]
        for i, service in enumerate(services):
            btn = QPushButton(service)
            btn.clicked.connect(lambda checked, s=service: self.handle_service(s))
            services_layout.addWidget(btn, i // 3, i % 3)

        main_layout.addWidget(services_card)
        main_layout.addStretch()
        self.setLayout(main_layout)

        self.fetch_user_data()

    def fetch_user_data(self):
        try:
            user_data = self.api_client.get_profile()
            analytics = self.api_client.get_analytics_summary()
            self.balance_label.setText(f"Balance: ${user_data.Balance:.2f}")
            self.analytics_label.setText(
                f"Monthly Spending: ${analytics.monthly_spending:.2f} | "
                f"Income: ${analytics.monthly_income:.2f} | "
                f"Transactions: {analytics.transaction_count}"
            )
        except Exception as e:
            self.balance_label.setText("Error loading data")
            self.analytics_label.setText(str(e))

    def handle_service(self, service):
        screen_map = {
            "Send Money": "Transfer",
            "Cards": "Cards",
            "Transactions": "Transactions",
            "Loan": "Loans"
        }
        screen = screen_map.get(service, "Dashboard")
        self.parent().switch_screen(screen)