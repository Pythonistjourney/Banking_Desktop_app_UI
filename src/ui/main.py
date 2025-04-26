import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Now import the application modules
from PySide6.QtWidgets import QApplication
from src.ui.navigation.navigation_manager import NavigationManager
from src.themes.theme_loader import ThemeLoader
from src.utils.config import load_config

def main():
    app = QApplication(sys.argv)
    
    # Load environment variables
    config = load_config()
    
    # Load theme
    theme_loader = ThemeLoader()
    theme = theme_loader.load_theme(config.get("DEFAULT_THEME", "dark"))
    with open("src/styles/global.qss", "r") as f:
        app.setStyleSheet(f.read())
    
    # Initialize navigation
    nav_manager = NavigationManager()
    nav_manager.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()