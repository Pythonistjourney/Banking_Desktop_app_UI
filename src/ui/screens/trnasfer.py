from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from src.api.client import APIClient
from src.schemas.schemas import TransferCreate
from decimal import Decimal

class TransferScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_client = APIClient()
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

        title = QLabel("Send Money")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        self.recipient_input = QLineEdit()
        self.recipient_input.setPlaceholderText("Enter recipient CNIC or email")
        card_layout.addWidget(self.recipient_input)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        card_layout.addWidget(self.amount_input)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description (optional)")
        card_layout.addWidget(self.description_input)

        self.error_label = QLabel("")
        self.error_label.setObjectName("error")
        self.error_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.error_label)

        transfer_button = QPushButton("Send")
        transfer_button.clicked.connect(self.handle_transfer)
        card_layout.addWidget(transfer_button)

        back_button = QPushButton("Back to Dashboard")
        back_button.setObjectName("link")
        back_button.clicked.connect(lambda: self.parent().switch_screen('Dashboard'))
        card_layout.addWidget(back_button)

        main_layout.addWidget(card, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def handle_transfer(self):
        if not self.recipient_input.text() or not self.amount_input.text():
            self.error_label.setText("Please fill in recipient and amount")
            return

        try:
            amount = Decimal(self.amount_input.text())
            transfer_data = TransferCreate(
                cnic=self.recipient_input.text() if '-' in self.recipient_input.text() else None,
                email=self.recipient_input.text() if '@' in self.recipient_input.text() else None,
                Amount=amount,
                Description=self.description_input.text() or None
            )
            response = self.api_client.create_transfer(transfer_data)
            self.error_label.setText(f"Transfer successful! Ref: {response.ReferenceNumber}")
        except ValueError:
            self.error_label.setText("Invalid amount format")
        except Exception as e:
            self.error_label.setText(f"Transfer failed: {str(e)}")