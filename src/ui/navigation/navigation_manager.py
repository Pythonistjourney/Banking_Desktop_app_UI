import sys
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QComboBox, QFrame
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QSize
from src.ui.screens.splash import SplashScreen
from src.ui.screens.login import LoginScreen
from src.ui.screens.signup import SignupScreen
from src.ui.screens.dashboard import DashboardScreen
from src.ui.screens.transfer import TransferScreen
from src.utils.theme_loader import ThemeLoader

class NavigationManager(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.setWindowTitle("AUT Finance Bank Desktop")
        self.setMinimumSize(800, 600)  # Set minimum window size
        self.theme_loader = ThemeLoader()
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Sidebar
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        self.nav_buttons = {
            'Dashboard': QPushButton('Dashboard'),
            'Login': QPushButton('Login'),
            'Signup': QPushButton('Signup'),
            'Transfer': QPushButton('Send Money'),
            'Transactions': QPushButton('Transactions'),
            'Cards': QPushButton('Cards'),
            'Loans': QPushButton('Loans'),
        }

        for name, button in self.nav_buttons.items():
            button.setObjectName("sidebar-button")
            button.clicked.connect(lambda checked, n=name: self.switch_screen(n))
            sidebar_layout.addWidget(button)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems([theme["name"] for theme in self.theme_loader.themes])
        self.theme_selector.currentTextChanged.connect(self.change_theme)
        sidebar_layout.addWidget(self.theme_selector)
        sidebar_layout.addStretch()

        main_layout.addWidget(sidebar)

        # Content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 10, 10, 10)
        self.stack = QStackedWidget()
        content_layout.addWidget(self.stack)
        main_layout.addWidget(content_widget)

        self.screens = {
            'Dashboard': DashboardScreen(self),
            'Login': LoginScreen(self),
            'Signup': SignupScreen(self),
            'Transfer': TransferScreen(self),
            'Transactions': QWidget(self),  # Placeholder
            'Cards': QWidget(self),        # Placeholder
            'Loans': QWidget(self),        # Placeholder
        }

        for screen in self.screens.values():
            self.stack.addWidget(screen)

        self.show_splash()

    def apply_theme(self):
        self.theme_loader.apply_theme(self.app)

    def change_theme(self, theme_name):
        theme_id = next(theme["id"] for theme in self.theme_loader.themes if theme["name"] == theme_name)
        self.theme_loader.switch_theme(theme_id, self.app)

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

    def resizeEvent(self, event):
        """Handle window resize events"""
        super().resizeEvent(event)
        # Maintain minimum aspect ratio
        size = event.size()
        min_width = 800
        min_height = 600
        if size.width() < min_width or size.height() < min_height:
            self.setMinimumSize(QSize(min_width, min_height))
        
        # Update content area size
        content_width = size.width() - 200  # Subtract sidebar width
        if content_width > 0:
            self.stack.setFixedWidth(content_width)

    def sizeHint(self):
        """Provide default size hint"""
        return QSize(1000, 700)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = NavigationManager(app)
    sys.exit(app.exec())