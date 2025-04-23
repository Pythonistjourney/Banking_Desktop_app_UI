from PySide6.QtWidgets import QMainWindow, QStackedWidget
from src.ui.login import LoginScreen
from src.ui.signup import SignupScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Banking App")
        self.resize(800, 600)
        
        # Create stacked widget for screen navigation
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # Initialize screens
        self.login_screen = LoginScreen(self)
        self.signup_screen = SignupScreen(self)
        
        # Add screens to stack
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.signup_screen)
        
        # Set initial screen
        self.stack.setCurrentWidget(self.login_screen)
    
    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_screen)
    
    def switch_to_signup(self):
        self.stack.setCurrentWidget(self.signup_screen)