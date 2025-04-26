from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt

# Screen dimensions for desktop
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Color palette (inspired by the image but adjusted per requirements)
COLORS = {
    'primary': QColor('#28A745'),  # Green for cards
    'secondary': QColor('#20C997'),  # Teal for hover effects
    'background': QColor('#FFFFFF'),  # White background
    'text': QColor('#2D3436'),  # Dark gray for text
    'placeholder': QColor('#A0AEC0'),  # Light gray for placeholders
    'danger': QColor('#DC3545'),  # Red for errors
    'white': QColor('#FFFFFF'),
    'black': QColor('#000000'),
    'gray': QColor('#E2E8F0'),  # Light gray for borders
    'button_gradient_start': QColor('#4A90E2'),  # Blue gradient start (from image)
    'button_gradient_end': QColor('#357ABD'),  # Blue gradient end (from image)
}

# Font sizes
FONT_SIZES = {
    'tiny': 12,
    'small': 14,
    'medium': 18,
    'large': 24,
    'xlarge': 36,
}

# Spacing
SPACING = {
    'tiny': 6,
    'small': 12,
    'medium': 20,
    'large': 30,
    'xlarge': 40,
}

# Fonts
FONTS = {
    'regular': QFont('Roboto', FONT_SIZES['medium']),
    'bold': QFont('Roboto', FONT_SIZES['medium'], QFont.Bold),
    'large': QFont('Roboto', FONT_SIZES['large'], QFont.Bold),
    'xlarge': QFont('Roboto', FONT_SIZES['xlarge'], QFont.Bold),
}

# Widget styles
def get_button_style():
    return f"""
        QPushButton {{
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {COLORS['button_gradient_start'].name()},
                stop:1 {COLORS['button_gradient_end'].name()});
            color: {COLORS['white'].name()};
            font-size: {FONT_SIZES['medium']}px;
            font-weight: bold;
            padding: {SPACING['medium']}px {SPACING['xlarge']}px;
            border-radius: 10px;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {COLORS['secondary'].name()};
        }}
        QPushButton:pressed {{
            background-color: {COLORS['button_gradient_end'].name()};
        }}
        QPushButton:disabled {{
            opacity: 0.6;
        }}
    """

def get_input_style():
    return f"""
        QLineEdit {{
            background-color: {COLORS['white'].name()};
            border: 1px solid {COLORS['gray'].name()};
            border-radius: 8px;
            padding: {SPACING['small']}px;
            font-size: {FONT_SIZES['medium']}px;
            color: {COLORS['text'].name()};
        }}
        QLineEdit:focus {{
            border: 2px solid {COLORS['primary'].name()};
        }}
        QLineEdit:placeholder {{
            color: {COLORS['placeholder'].name()};
        }}
    """

def get_label_style(size='medium'):
    weight = 'bold' if size in ['large', 'xlarge'] else 'normal'
    return f"""
        QLabel {{
            font-size: {FONT_SIZES[size]}px;
            color: {COLORS['text'].name()};
            font-weight: {weight};
        }}
    """

def get_card_style():
    return f"""
        QWidget {{
            background-color: {COLORS['primary'].name()};
            border-radius: 12px;
            padding: {SPACING['medium']}px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }}
    """