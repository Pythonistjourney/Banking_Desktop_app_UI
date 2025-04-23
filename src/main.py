import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QStackedWidget
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PySide6.QtGui import QFont, QPainter, QBrush, QColor

# Custom Background Widget with Shapes
class BackgroundWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Draw decorative circles
        painter.setBrush(QBrush(QColor(255, 255, 255, 50)))
        painter.drawEllipse(50, 50, 150, 150)
        painter.drawEllipse(600, 400, 100, 100)
        painter.drawEllipse(300, 500, 80, 80)

# Main Application Window
class BankingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AUT Unity Bank")
        self.setGeometry(100, 100, 800, 600)

        # Background widget with shapes
        self.background = BackgroundWidget(self)
        self.background.setGeometry(0, 0, 800, 600)

        # Stacked widget for navigation
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Initialize screens
        self.splash_screen = SplashScreen()
        self.login_screen = LoginScreen()
        self.signup_screen = SignupScreen()
        self.dashboard_screen = DashboardScreen()

        # Add screens to stack
        self.stack.addWidget(self.splash_screen)
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.signup_screen)  # Fixed the typo here
        self.stack.addWidget(self.dashboard_screen)

        # Start with splash screen
        self.stack.setCurrentWidget(self.splash_screen)

        # Connect navigation signals
        self.splash_screen.navigate_to_login.connect(self.show_login)
        self.login_screen.navigate_to_signup.connect(self.show_signup)
        self.login_screen.navigate_to_dashboard.connect(self.show_dashboard)
        self.signup_screen.navigate_to_dashboard.connect(self.show_dashboard)

        # Apply global styles
        self.setStyleSheet(self.load_styles())

    def load_styles(self):
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #26C6DA, stop:1 #4DD0E1);
            }
            QWidget#container {
                background: transparent;
            }
            QWidget#leftPanel {
                background: #1F2A44;
            }
            QWidget#rightPanel {
                background: white;
                border-radius: 10px;
            }
            QLabel {
                color: white;
                font-size: 18px;
            }
            QLabel#title {
                color: #26C6DA;
                font-size: 24px;
                font-weight: bold;
            }
            QLabel#subtitle {
                color: #26C6DA;
                font-size: 16px;
            }
            QLabel#formTitle {
                color: #1F2A44;
                font-size: 20px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #F5F5F5;
                border: 1px solid #E0E0E0;
                border-radius: 5px;
                padding: 8px;
                color: #1F2A44;
            }
            QPushButton {
                background-color: #26C6DA;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #4DD0E1;
            }
            QPushButton#link {
                background: none;
                color: #26C6DA;
                border: none;
            }
            QCheckBox {
                color: #1F2A44;
            }
        """

    def slide_transition(self, new_widget):
        current_widget = self.stack.currentWidget()
        new_widget.setGeometry(QRect(800, 0, 800, 600))
        self.stack.addWidget(new_widget)

        # Slide out current widget
        anim_out = QPropertyAnimation(current_widget, b"geometry")
        anim_out.setDuration(500)
        anim_out.setStartValue(QRect(0, 0, 800, 600))
        anim_out.setEndValue(QRect(-800, 0, 800, 600))

        # Slide in new widget
        anim_in = QPropertyAnimation(new_widget, b"geometry")
        anim_in.setDuration(500)
        anim_in.setStartValue(QRect(800, 0, 800, 600))
        anim_in.setEndValue(QRect(0, 0, 800, 600))

        # Start animations
        anim_out.start(QPropertyAnimation.DeleteWhenStopped)
        anim_in.start(QPropertyAnimation.DeleteWhenStopped)
        self.stack.setCurrentWidget(new_widget)

    def show_login(self):
        self.slide_transition(self.login_screen)

    def show_signup(self):
        self.slide_transition(self.signup_screen)

    def show_dashboard(self):
        self.slide_transition(self.dashboard_screen)

# Splash Screen
class SplashScreen(QWidget):
    from PySide6.QtCore import Signal
    navigate_to_login = Signal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Bank name label
        self.label = QLabel("AUT Unity Bank")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 36, QFont.Bold))
        self.label.setStyleSheet("opacity: 0;")
        layout.addWidget(self.label)

        # Loading label
        loading_label = QLabel("Loading...")
        loading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(loading_label)

        # Fade-in animation
        self.fade_anim = QPropertyAnimation(self.label, b"windowOpacity")
        self.fade_anim.setDuration(1000)
        self.fade_anim.setStartValue(0)
        self.fade_anim.setEndValue(1)
        self.fade_anim.start()

        # Timer to navigate to login screen
        QTimer.singleShot(2000, self.navigate_to_login.emit)

# Login Screen
class LoginScreen(QWidget):
    from PySide6.QtCore import Signal
    navigate_to_signup = Signal()
    navigate_to_dashboard = Signal()

    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.setObjectName("container")

        # Left panel
        left_panel = QWidget()
        left_panel.setObjectName("leftPanel")
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        title = QLabel("AUT Unity Bank")
        title.setObjectName("title")
        left_layout.addWidget(title)

        subtitle = QLabel("Your trusted banking partner")
        subtitle.setObjectName("subtitle")
        left_layout.addWidget(subtitle)

        left_layout.addStretch()

        # Right panel
        right_panel = QWidget()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        form_title = QLabel("User Login")
        form_title.setObjectName("formTitle")
        right_layout.addWidget(form_title)

        right_layout.addWidget(QLabel("Email"))
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        right_layout.addWidget(self.email)

        right_layout.addWidget(QLabel("Password"))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        right_layout.addWidget(self.password)

        remember = QCheckBox("Remember me")
        right_layout.addWidget(remember)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.navigate_to_dashboard.emit)
        right_layout.addWidget(login_btn)

        forgot_btn = QPushButton("Forgot Password?")
        forgot_btn.setObjectName("link")
        right_layout.addWidget(forgot_btn)

        right_layout.addStretch()

        # Add panels to main layout
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)

# Signup Screen
class SignupScreen(QWidget):
    from PySide6.QtCore import Signal
    navigate_to_dashboard = Signal()

    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.setObjectName("container")

        # Left panel
        left_panel = QWidget()
        left_panel.setObjectName("leftPanel")
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        title = QLabel("AUT Unity Bank")
        title.setObjectName("title")
        left_layout.addWidget(title)

        subtitle = QLabel("Your trusted banking partner")
        subtitle.setObjectName("subtitle")
        left_layout.addWidget(subtitle)

        left_layout.addStretch()

        # Right panel
        right_panel = QWidget()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        form_title = QLabel("Create Account")
        form_title.setObjectName("formTitle")
        right_layout.addWidget(form_title)

        right_layout.addWidget(QLabel("Username"))
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        right_layout.addWidget(self.username)

        right_layout.addWidget(QLabel("Email"))
        self.email = QLineEdit()
        self.email.setPlaceholderText("webmail@mail.com")
        right_layout.addWidget(self.email)

        right_layout.addWidget(QLabel("Password"))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        right_layout.addWidget(self.password)

        terms = QCheckBox("I agree with the terms and conditions")
        right_layout.addWidget(terms)

        signup_btn = QPushButton("Create my account")
        signup_btn.clicked.connect(self.navigate_to_dashboard.emit)
        right_layout.addWidget(signup_btn)

        right_layout.addStretch()

        # Add panels to main layout
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)

# Dashboard Screen
class DashboardScreen(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.setObjectName("container")

        # Left panel
        left_panel = QWidget()
        left_panel.setObjectName("leftPanel")
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        title = QLabel("AUT Unity Bank")
        title.setObjectName("title")
        left_layout.addWidget(title)

        subtitle = QLabel("Welcome back!")
        subtitle.setObjectName("subtitle")
        left_layout.addWidget(subtitle)

        left_layout.addStretch()

        # Right panel
        right_panel = QWidget()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        form_title = QLabel("Dashboard")
        form_title.setObjectName("formTitle")
        right_layout.addWidget(form_title)

        balance_label = QLabel("Balance: $10,000")
        right_layout.addWidget(balance_label)

        history_label = QLabel("Transaction History")
        right_layout.addWidget(history_label)
        history = QLabel("• Sent $500 to John - 04/22/2025\n• Received $1,000 from Jane - 04/20/2025")
        right_layout.addWidget(history)

        loans_label = QLabel("Loans")
        right_layout.addWidget(loans_label)
        loans = QLabel("• Personal Loan: $5,000 (Due: 12/2025)")
        right_layout.addWidget(loans)

        atm_label = QLabel("ATM Options")
        right_layout.addWidget(atm_label)
        atm_btn = QPushButton("Withdraw Cash")
        right_layout.addWidget(atm_btn)

        right_layout.addStretch()

        # Add panels to main layout
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankingApp()
    window.show()
    sys.exit(app.exec())