import sys
from PySide6.QtWidgets import QApplication
from src.ui.navigation.navigation_manager import NavigationManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = NavigationManager(app)  # Pass the app instance here
    sys.exit(app.exec())