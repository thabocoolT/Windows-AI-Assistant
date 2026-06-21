import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QFont


class Signals(QObject):
    update_text = Signal(str)
    update_status = Signal(str)
    close_app=Signal()


class NovaGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.signals.update_text.connect(self.set_text)
        self.signals.update_status.connect(self.set_status)
        self.signals.close_app.connect(self.close_window)  # ← add this
        self.init_ui()
       
    def init_ui(self):
        #Windows settings
        self.setWindowTitle("Nova")
        self.setFixedSize(300, 150)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Move to bottom right corner
        screen=QApplication.primaryScreen().geometry()
        self.move(
            screen.width() - 320,
            screen.height() -180
        )

        #layout
        layout=QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        self.setLayout(layout)

        #Status label (Sleeping/Listening)
        self.status_label=QLabel("Sleeping...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Segoe UI", 10))
        self.status_label.setStyleSheet("color: #888888")
        layout.addWidget(self.status_label)

        #Main text label
        self.text_label=QLabel("Nova")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.text_label.setWordWrap(True)
        self.text_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.text_label)

        # Background style
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(20, 20, 20, 220);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 30);
            }
        """)

    def set_text(self, text):
        self.text_label.setText(text)

    def set_status(self, status):
        colors={
            "Sleeping...": "#777777",
            "Listening...": "#00BFFF",
            "Thinking...":"#FFD700",
            "Speaking...":"#00ff99",
            "Shutting...":"#FF4444"

        }
        color=colors.get(status,"#ffffff")
        self.status_label.setText(status)
        self.status_label.setStyleSheet(
            f"color:{color}; font-size:11pt;"
        )

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(
            self.pos() +
            event.globalPosition().toPoint() -
            self.drag_pos
        )
        self.drag_pos = event.globalPosition().toPoint()

    def closeEvent(self, event):
        QApplication.quit()
        event.accept()

    def close_window(self):
        self.close()

   


