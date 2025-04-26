from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox
)
from PySide6.QtCore import Qt

class TransferScreen(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        title = QLabel("Send Money")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Recipient Account field
        self.recipient_input = QLineEdit()
        self.recipient_input.setPlaceholderText("Recipient Account Number")
        layout.addWidget(self.recipient_input)

        # Amount field
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        layout.addWidget(self.amount_input)

        # Description field
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Description (Optional)")
        layout.addWidget(self.description_input)

        # Send button
        send_button = QPushButton("Send Money")
        send_button.clicked.connect(self.handle_transfer)
        layout.addWidget(send_button)

    def handle_transfer(self):
        recipient = self.recipient_input.text()
        amount = self.amount_input.text()
        description = self.description_input.text()

        if not recipient or not amount:
            QMessageBox.warning(self, "Error", "Recipient and amount are required")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount")
            return

        # TODO: Implement actual transfer logic here
        QMessageBox.information(self, "Success", "Transfer initiated successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.recipient_input.clear()
        self.amount_input.clear()
        self.description_input.clear()