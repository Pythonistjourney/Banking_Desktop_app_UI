from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QParallelAnimationGroup, Signal, QEasingCurve, QSize
from PySide6.QtGui import QFont, QColor, QPixmap, QPainter, QLinearGradient, QBrush

class AnimatedText(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)
        self._scale = 0.8
        self._spacing = 0

    def animate(self, duration=800, delay=0, final_delay=200):
        # Fade in animation
        opacity_anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        opacity_anim.setDuration(duration)
        opacity_anim.setStartValue(0)
        opacity_anim.setEndValue(1)
        opacity_anim.setEasingCurve(QEasingCurve.OutQuint)

        # Scale animation
        scale_anim = QPropertyAnimation(self, b"geometry")
        start_geo = self.geometry()
        scale_anim.setDuration(duration)
        scale_anim.setStartValue(start_geo.adjusted(50, 50, -50, -50))
        scale_anim.setEndValue(start_geo)
        scale_anim.setEasingCurve(QEasingCurve.OutBack)

        group = QParallelAnimationGroup()
        group.addAnimation(opacity_anim)
        group.addAnimation(scale_anim)
        
        QTimer.singleShot(delay, group.start)

        # Fade out after showing
        fade_out = QPropertyAnimation(self.opacity_effect, b"opacity")
        fade_out.setDuration(500)
        fade_out.setStartValue(1)
        fade_out.setEndValue(0)
        fade_out.setEasingCurve(QEasingCurve.InCubic)
        QTimer.singleShot(delay + duration + final_delay, fade_out.start)

class SplashScreen(QWidget):
    finished = Signal()

    def __init__(self, parent=None):  # Add parent parameter with default None
        super().__init__(parent)  # Pass parent to super().__init__
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup_ui()
        self.center_window()
        
    def setup_ui(self):
        self.setFixedSize(800, 500)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(60, 60, 60, 60)
        layout.setSpacing(40)

        # Create logo
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setFixedSize(120, 120)
        self.create_logo()
        layout.addWidget(self.logo_label, 0, Qt.AlignCenter)

        # Create animated text labels
        self.welcome_text = AnimatedText("Welcome")
        self.secure_text = AnimatedText("Secure Banking")
        self.bank_text = AnimatedText("GREENBANK")

        # Style labels
        gradient_font = QFont("Montserrat", 48, QFont.Bold)
        bank_font = QFont("Montserrat", 56, QFont.Black)
        
        self.welcome_text.setFont(gradient_font)
        self.secure_text.setFont(gradient_font)
        self.bank_text.setFont(bank_font)
        
        # Apply gradients
        for label, colors in [
            (self.welcome_text, ("#006400", "#00A300")),
            (self.secure_text, ("#006400", "#00A300")),
            (self.bank_text, ("#003300", "#00CC00"))
        ]:
            self.apply_gradient(label, colors[0], colors[1])
            layout.addWidget(label, 0, Qt.AlignCenter)

        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 50))
        shadow.setOffset(0, 2)
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("background-color: white; border-radius: 24px;")

    def create_logo(self):
        size = self.logo_label.size()
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw circle
        painter.setBrush(QBrush(QColor("#008000")))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(pixmap.rect().adjusted(5, 5, -5, -5))
        
        # Draw text
        painter.setFont(QFont("Montserrat", 36, QFont.Bold))
        painter.setPen(QColor(Qt.white))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "GB")
        painter.end()
        
        self.logo_label.setPixmap(pixmap)

    def apply_gradient(self, label, color1, color2):
        pixmap = QPixmap(label.sizeHint())
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        gradient = QLinearGradient(0, 0, pixmap.width(), 0)
        gradient.setColorAt(0, QColor(color1))
        gradient.setColorAt(1, QColor(color2))
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(gradient)
        painter.setFont(label.font())
        painter.drawText(pixmap.rect(), Qt.AlignCenter, label.text())
        painter.end()
        
        label.setPixmap(pixmap)

    def center_window(self):
        screen = self.screen().geometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )

    def showEvent(self, event):
        super().showEvent(event)
        # Start animation sequence
        self.welcome_text.animate(800, 0, 400)
        self.secure_text.animate(800, 1200, 400)
        self.bank_text.animate(800, 2400, 600)
        # Finish splash screen
        QTimer.singleShot(4000, self.finish_splash)

    def finish_splash(self):
        self.finished.emit()
        self.close()