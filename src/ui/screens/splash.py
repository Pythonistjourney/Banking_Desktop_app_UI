from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation

class SplashScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1000, 700)
        self.animations = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(40)

        # Animated welcome text
        welcome_text = "Welcome to AUT Finance Bank..."
        self.label_container = QWidget()
        label_layout = QHBoxLayout(self.label_container)
        label_layout.setSpacing(6)
        label_layout.setAlignment(Qt.AlignCenter)

        for char in welcome_text:
            label = QLabel(char)
            label.setObjectName("title")
            label.setProperty("opacity", 0.0)
            label_layout.addWidget(label)

            # Animation for each character
            anim = QPropertyAnimation(label, b"opacity")
            anim.setDuration(500)
            anim.setStartValue(0.0)
            anim.setEndValue(1.0)
            self.animations.append(anim)

        layout.addWidget(self.label_container)
        layout.addStretch()
        self.setLayout(layout)

        # Start animations
        self.start_animations()

    def start_animations(self):
        for i, anim in enumerate(self.animations):
            QTimer.singleShot(i * 100, lambda: anim.start())

        # Transition to login screen after animations
        QTimer.singleShot(len(self.animations) * 100 + 2000, self.finish_splash)

    def finish_splash(self):
        self.parent().switch_screen('Login')
        self.close()

    def opacity(self, widget, value):
        widget.setStyleSheet(f"opacity: {value};")