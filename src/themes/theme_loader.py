from src.styles.global_styles import GlobalStyles
from dataclasses import replace

class ThemeLoader:
    def __init__(self):
        self.global_styles = GlobalStyles()
        self._original_styles = GlobalStyles()

    def load_theme(self, theme_name: str) -> str:
        # Reset to original styles before applying new theme
        self.global_styles = replace(self._original_styles)
        
        themes = {
            "light": self.global_styles.get_stylesheet(),
            "dark": self._get_dark_theme()
        }
        return themes.get(theme_name, themes["light"])

    def _get_dark_theme(self) -> str:
        # Create new colors for dark theme without modifying original
        dark_colors = replace(self.global_styles.colors,
            background="#1E1E1E",
            surface="#2D2D2D",
            text_primary="#FFFFFF",
            text_secondary="#CCCCCC",
            primary="#3700B3",
            secondary="#03DAC6"
        )
        self.global_styles.colors = dark_colors
        return self.global_styles.get_stylesheet()