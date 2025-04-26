import json
import os
from PySide6.QtWidgets import QApplication

class ThemeLoader:
    def __init__(self, themes_file="src/themes/themes.json"):
        self.themes_file = themes_file
        self.themes = self.load_themes()
        self.current_theme = "dark"  # Default theme

    def load_themes(self):
        try:
            with open(self.themes_file, 'r') as f:
                return json.load(f).get("themes", [])
        except Exception as e:
            print(f"Error loading themes: {e}")
            return []

    def get_theme(self, theme_id):
        for theme in self.themes:
            if theme["id"] == theme_id:
                return theme
        return self.themes[0] if self.themes else {}

    def apply_theme(self, app: QApplication, theme_id: str = None):
        if theme_id:
            self.current_theme = theme_id
        theme = self.get_theme(self.current_theme)
        variables = theme.get("variables", {})

        # Load global stylesheet and replace variables
        with open("src/styles/global.qss", "r") as f:
            stylesheet = f.read()

        for var, value in variables.items():
            stylesheet = stylesheet.replace(f"@{var}", value)

        app.setStyleSheet(stylesheet)

    def switch_theme(self, theme_id: str, app: QApplication):
        self.apply_theme(app, theme_id)