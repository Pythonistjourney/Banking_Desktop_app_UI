from dataclasses import dataclass, field
from typing import Dict

@dataclass
class ThemeColors:
    primary: str = "#1E3D59"
    secondary: str = "#FF6E40"
    background: str = "#FFFFFF"
    surface: str = "#F5F5F5"
    text_primary: str = "#333333"
    text_secondary: str = "#666666"
    error: str = "#DC3545"
    success: str = "#28A745"
    warning: str = "#FFC107"
    info: str = "#17A2B8"

@dataclass
class Dimensions:
    spacing_xs: int = 4
    spacing_sm: int = 8
    spacing_md: int = 16
    spacing_lg: int = 24
    spacing_xl: int = 32
    border_radius: int = 8
    icon_size_sm: int = 16
    icon_size_md: int = 24
    icon_size_lg: int = 32

@dataclass
class Typography:
    font_family: str = "Segoe UI"
    font_size_sm: int = 12
    font_size_md: int = 14
    font_size_lg: int = 16
    font_size_xl: int = 20
    font_weight_normal: int = 400
    font_weight_bold: int = 700

@dataclass
class GlobalStyles:
    colors: ThemeColors = field(default_factory=ThemeColors)
    dimensions: Dimensions = field(default_factory=Dimensions)
    typography: Typography = field(default_factory=Typography)

    def get_stylesheet(self) -> str:
        return f"""
            QWidget {{
                font-family: {self.typography.font_family};
                font-size: {self.typography.font_size_md}px;
            }}

            QPushButton {{
                background-color: {self.colors.primary};
                color: white;
                border: none;
                border-radius: {self.dimensions.border_radius}px;
                padding: {self.dimensions.spacing_sm}px {self.dimensions.spacing_md}px;
                font-weight: {self.typography.font_weight_bold};
            }}

            QPushButton:hover {{
                background-color: {self.colors.secondary};
            }}

            QLineEdit {{
                padding: {self.dimensions.spacing_sm}px;
                border: 1px solid {self.colors.text_secondary};
                border-radius: {self.dimensions.border_radius}px;
                background-color: {self.colors.surface};
            }}

            QLabel {{
                color: {self.colors.text_primary};
            }}
        """