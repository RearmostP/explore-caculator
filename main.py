from PyQt5 import QtCore, QtGui, QtWidgets


class RoundedWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # הגדרות בסיסיות
        self.setWindowTitle("מחשב הוצאות")
        self.resize(400, 450)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # === אלמנט רקע עם פינות מעוגלות ===
        self.bg = QtWidgets.QFrame(self)
        self.bg.setGeometry(0, 0, 400, 450)
        self.bg.setStyleSheet("""
            QFrame {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #2e2e2e, stop:1 #3a3a3a
                );
                border-radius: 20px;
            }
        """)

        # === אייקון שמאל עליון ===
        self.icon_label = QtWidgets.QLabel(self.bg)
        self.icon_label.setGeometry(QtCore.QRect(10, 10, 28, 28))
        pixmap = QtGui.QPixmap("app_icon.svg")
        self.icon_label.setPixmap(pixmap.scaled(28, 28, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.icon_label.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # === כפתור סגירה ===
        self.close_btn = QtWidgets.QPushButton("×", self.bg)
        self.close_btn.setGeometry(QtCore.QRect(360, 10, 30, 30))
        self.close_btn.setStyleSheet("""
            QPushButton {
                color: #cccccc;
                background-color: transparent;
                border: none;
                font: 16pt "Segoe UI";
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #e81123;
                color: white;
            }
        """)
        self.close_btn.clicked.connect(self.close)

        # === כותרת ===
        self.main_label = QtWidgets.QLabel("מחשב הוצאות", self.bg)
        self.main_label.setGeometry(QtCore.QRect(80, 50, 250, 80))
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setStyleSheet("color: white; font: bold 20pt 'Segoe UI Variable Display';")

        # === כפתורים ===
        button_style = """
            QPushButton {
                color: #e6e6e6;
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #4a4a4a, stop:1 #2e2e2e
                );
                border: 1px solid #5a5a5a;
                border-radius: 12px;
                padding: 10px;
                font: 12pt "Segoe UI";
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #5b5b5b, stop:1 #3a3a3a
                );
                border: 1px solid #7d7d7d;
            }
            QPushButton:pressed {
                background-color: #232323;
                border: 1px solid #999;
                transform: scale(0.97);
            }
        """

        self.creat_explore = QtWidgets.QPushButton("יצירת\nרשימה חדשה", self.bg)
        self.creat_explore.setGeometry(QtCore.QRect(230, 210, 130, 60))
        self.creat_explore.setStyleSheet(button_style)

        self.see_explores = QtWidgets.QPushButton("צפייה\nברשימות", self.bg)
        self.see_explores.setGeometry(QtCore.QRect(40, 210, 130, 60))
        self.see_explores.setStyleSheet(button_style)

        self.settings = QtWidgets.QPushButton("הגדרות", self.bg)
        self.settings.setGeometry(QtCore.QRect(130, 310, 130, 60))
        self.settings.setStyleSheet(button_style)

        # אפקט צל
        for btn in [self.creat_explore, self.see_explores, self.settings]:
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setColor(QtGui.QColor(0, 0, 0, 150))
            shadow.setOffset(0, 3)
            btn.setGraphicsEffect(shadow)

        # מאפשר גרירה של החלון ע"י גרירת האזור העליון
        self.oldPos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = RoundedWindow()
    w.show()
    sys.exit(app.exec_())
