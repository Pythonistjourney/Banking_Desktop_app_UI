from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal, QTimer

class SplashScreen(QWidget):
    finished = Signal()  # Add the finished signal

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup_ui()
        self.start_timer()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add splash screen content
        title = QLabel("AUT Finance Bank")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)

        # Set fixed size for splash screen
        self.setFixedSize(400, 300)
        # Center the splash screen
        self.center_on_screen()

    def center_on_screen(self):
        from PySide6.QtWidgets import QApplication
        screen = QApplication.primaryScreen().geometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )

    def start_timer(self):
        # Show splash screen for 2 seconds
        QTimer.singleShot(2000, self.on_timeout)

    def on_timeout(self):
        self.finished.emit()  # Emit the finished signal
        self.close()