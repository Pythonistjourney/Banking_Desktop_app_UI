import json
import os
from pathlib import Path

class ThemeLoader:
    def __init__(self):
        self._themes = None
        self.load_themes()

    def load_themes(self):
        """Load themes from the themes directory"""
        themes_dir = Path(__file__).parent / 'themes'
        self._themes = []
        
        # Default dark theme
        self._themes.append({
            "name": "Dark",
            "styles": {
                "background": "#2b2b2b",
                "text": "#ffffff",
                "button": "#404040",
                "button_text": "#ffffff",
                "input_background": "#3b3b3b",
                "input_text": "#ffffff",
                "border": "#505050"
            }
        })
        
        # Default light theme
        self._themes.append({
            "name": "Light",
            "styles": {
                "background": "#ffffff",
                "text": "#000000",
                "button": "#e0e0e0",
                "button_text": "#000000",
                "input_background": "#f5f5f5",
                "input_text": "#000000",
                "border": "#cccccc"
            }
        })

    @property
    def themes(self):
        """Return the list of available themes"""
        return self._themes

    def get_theme_by_name(self, name):
        """Get a theme by its name"""
        for theme in self._themes:
            if theme["name"].lower() == name.lower():
                return theme
        return None