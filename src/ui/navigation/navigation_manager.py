from PySide6.QtWidgets import (
    QMainWindow, 
    QStackedWidget, 
    QVBoxLayout, 
    QHBoxLayout,  # Added this import
    QWidget, 
    QPushButton
)
from PySide6.QtCore import Qt
from src.ui.screens.splash_screen import SplashScreen
from src.ui.screens.login_screen import LoginScreen
from src.ui.screens.signup.signup_step1 import SignupStep1
from src.ui.screens.dashboard_screen import DashboardScreen

class NavigationManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AUT Finance Bank Desktop")
        self.setGeometry(100, 100, 1000, 700)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Navigation buttons (temporary for testing)
        nav_bar = QWidget()
        nav_layout = QHBoxLayout(nav_bar)
        self.nav_buttons = {
            'Dashboard': QPushButton('Dashboard'),
            'Login': QPushButton('Login'),
            'Signup': QPushButton('Signup'),
        }

        for name, button in self.nav_buttons.items():
            button.clicked.connect(lambda checked, n=name: self.switch_screen(n))
            nav_layout.addWidget(button)

        layout.addWidget(nav_bar)

        # Stacked widget for screens
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Initialize screens
        self.screens = {
            'Dashboard': DashboardScreen(self),
            'Login': LoginScreen(self),
            'Signup': SignupStep1(self),
            'ForgotPassword': QWidget(self),
        }

        for screen in self.screens.values():
            self.stack.addWidget(screen)

        # Show splash screen differently
        self.show_splash()

    def show_splash(self):
        self.splash = SplashScreen()
        self.splash.finished.connect(self.on_splash_finished)
        self.splash.show()

    def on_splash_finished(self):
        self.switch_screen('Login')
        self.show()

    def switch_screen(self, screen_name):
        if screen_name in self.screens:
            self.stack.setCurrentWidget(self.screens[screen_name])
            self.show()