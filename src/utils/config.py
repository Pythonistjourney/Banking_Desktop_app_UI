import os
import json
from pathlib import Path

def load_config():
    """
    Load configuration from config.json file or return default config
    """
    config_path = Path(__file__).parent.parent.parent / "config.json"
    default_config = {
        "DEFAULT_THEME": "dark",
        "WINDOW_SIZE": {
            "width": 1000,
            "height": 700
        },
        "APP_NAME": "AUT Finance Bank Desktop",
        "DEMO_MODE": True
    }

    try:
        if config_path.exists():
            with open(config_path, "r") as f:
                return json.load(f)
        else:
            # Create default config file if it doesn't exist
            with open(config_path, "w") as f:
                json.dump(default_config, f, indent=4)
            return default_config
    except Exception as e:
        print(f"Error loading config: {e}")
        return default_config

class ThemeLoader:
    def load_theme(self, theme_name):
        # Placeholder: In a real app, this would load theme-specific settings
        return {"theme": theme_name}