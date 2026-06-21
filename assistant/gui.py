import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import (
    Qt,
    Signal,
    QObject,
    QTimer
)

from PySide6.QtGui import (
    QFont,
    QColor,
    QPainter,
    QBrush
)


class Signals(QObject):
    update_text = Signal(str)
    update_status = Signal(str)
    close_app = Signal()


class NovaGUI(QWidget):

    def __init__(self):

        super().__init__()

        self.signals = Signals()

        self.signals.update_text.connect(
            self.set_text
        )

        self.signals.update_status.connect(
            self.set_status
        )

        self.signals.close_app.connect(
            self.close_window
        )

        self.current_status = "Sleeping..."

        self.glow = 0
        self.orbs_size=130
        self.target_size=130

        self.direction = 1

        self.init_ui()

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(
            35
        )

    def init_ui(self):

        # Window settings

        self.setWindowTitle("Nova")

        self.setFixedSize(
            320,
            260
        )

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            |
            Qt.FramelessWindowHint
            |
            Qt.Tool
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        # Bottom right

        screen = (
            QApplication
            .primaryScreen()
            .geometry()
        )

        self.move(
            screen.width() - 350,
            screen.height() - 320
        )

        # Layout

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        layout.setSpacing(
            10
        )

        self.setLayout(
            layout
        )

        # Orb

        self.orb = QLabel()

        self.orb.setFixedSize(
            130,
            130
        )

        layout.addWidget(
            self.orb,
            alignment=Qt.AlignCenter
        )

        # Status

        self.status_label = QLabel(
            "Sleeping..."
        )

        self.status_label.setAlignment(
            Qt.AlignCenter
        )

        self.status_label.setFont(
            QFont(
                "Segoe UI",
                10
            )
        )

        layout.addWidget(
            self.status_label
        )

        # Main text

        self.text_label = QLabel(
            "Nova"
        )

        self.text_label.setAlignment(
            Qt.AlignCenter
        )

        self.text_label.setFont(
            QFont(
                "Segoe UI",
                13,
                QFont.Bold
            )
        )

        self.text_label.setWordWrap(
            True
        )

        layout.addWidget(
            self.text_label
        )

        self.set_status(
            "Sleeping..."
        )

    def animate(self):

        if (
            self.orbs_size
            <
            self.target_size
        ):

            self.orbs_size += 3

        elif (
            self.orbs_size
            >
            self.target_size
        ):

            self.orbs_size -= 3


        self.glow += (
            self.direction
            * 4
        )

        if self.glow > 70:

            self.direction = -1

        elif self.glow < 0:

            self.direction = 1


        self.update()

    def paintEvent(
        self,
        event
    ):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        # Glass panel

        panel = QColor(
            20,
            20,
            20,
            220
        )

        painter.setBrush(
            QBrush(panel)
        )

        painter.setPen(
            Qt.NoPen
        )

        painter.drawRoundedRect(
            self.rect(),
            28,
            28
        )

        colors = {

            "Sleeping...":
            "#777777",

            "Listening...":
            "#00BFFF",

            "Thinking...":
            "#FFD700",

            "Speaking...":
            "#00FF99",

            "Shutting down...":
            "#FF4444"
        }

        color = QColor(
            colors.get(
                self.current_status,
                "#ffffff"
            )
        )

        color.setAlpha(
            120
            +
            self.glow
        )

        painter.setBrush(
            QBrush(color)
        )
        

       # Dynamic orb size


        x = (
            self.width()
            -
            self.orbs_size
        ) // 2

        y = 35

        painter.drawEllipse(
            x,
            y,
            self.orbs_size,
            self.orbs_size
        )

    def set_text(
        self,
        text
    ):

        self.text_label.setText(
            text
        )

    def set_status(
        self,
        status
    ):

        self.current_status = status
        sizes = {

            "Sleeping...":
            120,

            "Listening...":
            140,

            "Thinking...":
            165,

            "Speaking...":
            185,

            "Shutting down...":
            110
        }

        self.target_size = (
            sizes.get(
                status,
                130
            )
        )

        colors = {

            "Sleeping...":
            "#777777",

            "Listening...":
            "#00BFFF",

            "Thinking...":
            "#FFD700",

            "Speaking...":
            "#00FF99",

            "Shutting down...":
            "#FF4444"
        }

        color = (
            colors.get(
                status,
                "#ffffff"
            )
        )

        self.status_label.setText(
            status
        )

        self.status_label.setStyleSheet(
            f"""
color:{color};
font-size:11pt;
"""
        )

        self.update()

    def mousePressEvent(
        self,
        event
    ):

        self.drag_pos = (
            event
            .globalPosition()
            .toPoint()
        )

    def mouseMoveEvent(
        self,
        event
    ):

        self.move(

            self.pos()

            +

            event
            .globalPosition()
            .toPoint()

            -

            self.drag_pos

        )

        self.drag_pos = (

            event
            .globalPosition()
            .toPoint()

        )

    def closeEvent(
        self,
        event
    ):

        QApplication.quit()

        event.accept()

    def close_window(
        self
    ):

        self.close()