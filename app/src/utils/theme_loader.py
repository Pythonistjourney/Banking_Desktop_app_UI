class ThemeLoader:
    def __init__(self):
        self._themes = [
            {
                "id": 1,
                "name": "Light",
                "styles": {
                    "background": "#ffffff",
                    "text": "#000000",
                    "button": "#e0e0e0",
                    "button_text": "#000000",
                    "input_background": "#f5f5f5",
                    "input_text": "#000000",
                    "border": "#cccccc",
                    "sidebar": "#f0f0f0"
                }
            },
            {
                "id": 2,
                "name": "Dark",
                "styles": {
                    "background": "#2b2b2b",
                    "text": "#ffffff",
                    "button": "#404040",
                    "button_text": "#ffffff",
                    "input_background": "#3b3b3b",
                    "input_text": "#ffffff",
                    "border": "#505050",
                    "sidebar": "#1b1b1b"
                }
            }
        ]

    @property
    def themes(self):
        return self._themes

    def get_theme_by_id(self, theme_id):
        return next((theme for theme in self._themes if theme["id"] == theme_id), None)

    def apply_theme(self, app):
        # Apply default theme (Light)
        self.switch_theme(1, app)

    def switch_theme(self, theme_id, app):
        theme = self.get_theme_by_id(theme_id)
        if not theme:
            return

        styles = theme["styles"]
        app.setStyleSheet(f"""
            QMainWindow {{
                background-color: {styles["background"]};
                color: {styles["text"]};
            }}
            QWidget {{
                background-color: {styles["background"]};
                color: {styles["text"]};
            }}
            QPushButton {{
                background-color: {styles["button"]};
                color: {styles["button_text"]};
                border: 1px solid {styles["border"]};
                padding: 5px;
                border-radius: 3px;
            }}
            QLineEdit {{
                background-color: {styles["input_background"]};
                color: {styles["input_text"]};
                border: 1px solid {styles["border"]};
                padding: 5px;
                border-radius: 3px;
            }}
            QComboBox {{
                background-color: {styles["input_background"]};
                color: {styles["input_text"]};
                border: 1px solid {styles["border"]};
                padding: 5px;
                border-radius: 3px;
            }}
            #sidebar {{
                background-color: {styles["sidebar"]};
                border-right: 1px solid {styles["border"]};
            }}
            #sidebar-button {{
                text-align: left;
                padding: 10px;
                border-radius: 0;
                border: none;
                background-color: transparent;
            }}
            #sidebar-button:hover {{
                background-color: {styles["button"]};
            }}
        """)

    def load_theme(self, theme_name):
        # Placeholder: In a real app, this would load theme-specific settings
        return {"theme": theme_name}