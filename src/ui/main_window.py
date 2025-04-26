from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Qt
from .screens.splash import SplashScreen
from .screens.login import LoginScreen
from .screens.dashboard import DashboardScreen
from .screens.signup import SignupScreen
from .navigation.navigation_manager import NavigationManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Banking Desktop App")
        self.setMinimumSize(1200, 800)
        
        # Create stacked widget for screens
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize screens
        self.splash_screen = SplashScreen()
        self.login_screen = LoginScreen()
        self.signup_screen = SignupScreen()
        self.dashboard_screen = DashboardScreen()
        
        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.splash_screen)
        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.signup_screen)
        self.stacked_widget.addWidget(self.dashboard_screen)
        
        # Initialize navigation manager
        self.navigation_manager = NavigationManager(self.stacked_widget)
        
        # Connect signals
        self.splash_screen.finished.connect(self.show_login)
        self.login_screen.signup_requested.connect(self.show_signup)
        self.login_screen.login_successful.connect(self.show_dashboard)
        self.signup_screen.back_to_login.connect(self.show_login)
        self.signup_screen.signup_successful.connect(self.show_dashboard)
        
        # Show splash screen initially
        self.show_splash()
    
    def show_splash(self):
        self.stacked_widget.setCurrentWidget(self.splash_screen)
        self.splash_screen.start_animation()
    
    def show_login(self):
        self.stacked_widget.setCurrentWidget(self.login_screen)
    
    def show_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_screen)
    
    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_screen) 