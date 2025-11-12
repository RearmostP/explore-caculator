from PyQt5 import QtWidgets, QtGui, QtCore
from core.base_window import BaseWindow
from core.app_manager import AppManager
from settings_window import SettingsDialog
from windows.explore_list import ExploreListWindow
from windows.create_list import CreateListWindow


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.manager = AppManager()
        self.lang = self.manager.get_language()
        self.theme = self.manager.get_theme()

        # === הגדרות חלון בסיסיות ===
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)  # שקיפות לפינות
        self.resize(400, 450)

        # === רקע עם פינות מעוגלות ===
        self.bg = QtWidgets.QFrame(self)
        self.bg.setGeometry(5, 5, 390, 440)  # רווח קטן כדי שהפינות השקופות יהיו גלויות

        # === צל חיצוני עדין ===
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(35)
        shadow.setOffset(0, 0)
        shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.setGraphicsEffect(shadow)

        # === אייקון שמאל עליון ===
        self.icon_label = QtWidgets.QLabel(self.bg)
        self.icon_label.setGeometry(QtCore.QRect(10, 10, 28, 28))
        pixmap = QtGui.QPixmap("images/app_icon.svg")
        self.icon_label.setPixmap(pixmap.scaled(28, 28, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

        # === כפתור סגירה ===
        self.close_btn = QtWidgets.QPushButton("×", self.bg)
        self.close_btn.setGeometry(QtCore.QRect(360, 10, 30, 30))
        self.close_btn.setStyleSheet("""
            QPushButton {
                color: #ccc;
                background-color: transparent;
                border: none;
                font: 16pt 'Segoe UI';
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #e81123;
                color: white;
            }
        """)
        self.close_btn.clicked.connect(self.close)

        # === כפתור מזעור ===
        self.min_btn = QtWidgets.QPushButton("—", self.bg)
        self.min_btn.setGeometry(QtCore.QRect(320, 10, 30, 30))
        self.min_btn.setStyleSheet("""
            QPushButton {
                color: #ccc;
                background-color: transparent;
                border: none;
                font: 14pt 'Segoe UI';
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                color: white;
            }
        """)
        self.min_btn.clicked.connect(self.showMinimized)

        # === כותרת ראשית ===
        self.main_label = QtWidgets.QLabel(self.lang["app_title"], self.bg)
        self.main_label.setGeometry(QtCore.QRect(80, 50, 250, 80))
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)

        # === כפתורים עיקריים ===
        self.creat_explore = QtWidgets.QPushButton(self.lang["create_list"], self.bg)
        self.creat_explore.setGeometry(QtCore.QRect(230, 210, 130, 60))
        self.creat_explore.clicked.connect(self.open_create_list_window)

        self.see_explores = QtWidgets.QPushButton(self.lang["see_lists"], self.bg)
        self.see_explores.setGeometry(QtCore.QRect(40, 210, 130, 60))
        self.see_explores.clicked.connect(self.open_explore_window)

        self.settings = QtWidgets.QPushButton(self.lang["settings"], self.bg)
        self.settings.setGeometry(QtCore.QRect(130, 310, 130, 60))
        self.settings.clicked.connect(self.open_settings)

        # === החלת עיצוב התחלתי ===
        self.apply_theme_and_lang()
        self.fade_transition()

        self.oldPos = None

    # === עיצוב כהה ובהיר ===
    def apply_theme_and_lang(self):
        """החלת עיצוב ושפה על כל האלמנטים"""
        if self.theme == "dark":
            bg_color = """
                QFrame {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:1,
                        stop:0 #2b2b2b, stop:1 #3a3a3a
                    );
                    border-radius: 20px;
                }
            """
            text_color = "#fff"
            btn_bg = "#3a3a3a"
            btn_hover = "#4a4a4a"
            btn_pressed = "#2e2e2e"
            border_color = "#5a5a5a"
        else:
            bg_color = """
                QFrame {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:1,
                        stop:0 #f4f4f4, stop:1 #d6d6d6
                    );
                    border-radius: 20px;
                }
            """
            text_color = "#222"
            btn_bg = "#f1f1f1"
            btn_hover = "#e4e4e4"
            btn_pressed = "#d0d0d0"
            border_color = "#bcbcbc"

        # החלת צבע רקע
        self.bg.setStyleSheet(bg_color)

        # עדכון טקסט
        self.main_label.setText(self.lang["app_title"])
        self.main_label.setStyleSheet(
            f"color: {text_color}; font: 800 22pt 'Segoe UI Variable Display'; letter-spacing: 1px;"
        )

        # עיצוב כפתורים
        button_style = f"""
            QPushButton {{
                color: {text_color};
                background-color: {btn_bg};
                border: 1px solid {border_color};
                border-radius: 12px;
                padding: 10px;
                font: 12pt 'Segoe UI';
            }}
            QPushButton:hover {{
                background-color: {btn_hover};
            }}
            QPushButton:pressed {{
                background-color: {btn_pressed};
            }}
        """

        for btn in [self.creat_explore, self.see_explores, self.settings]:
            btn.setStyleSheet(button_style)

        # אפקט זוהר עדין על הכותרת
        glow = QtWidgets.QGraphicsDropShadowEffect()
        glow.setColor(QtGui.QColor(255, 255, 255, 180) if self.theme == "dark" else QtGui.QColor(0, 0, 0, 120))
        glow.setBlurRadius(30)
        glow.setOffset(0, 0)
        self.main_label.setGraphicsEffect(glow)

    # === אפקט פתיחה חלק ===
    def fade_transition(self, duration=500):
        """אנימציית Fade-In עדינה בעת פתיחת החלון"""
        self.setWindowOpacity(0)
        anim = QtCore.QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(duration)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        anim.start()
        self.anim = anim

    # === פתיחת חלונות אחרים ===
    def open_explore_window(self):
        self.explore_window = ExploreListWindow()
        self.explore_window.show()
        self.close()

    def open_create_list_window(self):
        self.create_window = CreateListWindow()
        self.create_window.show()
        self.close()

    def open_settings(self):
        dlg = SettingsDialog(self, self.manager.config["language"], self.manager.config["theme"])
        if dlg.exec_() == QtWidgets.QDialog.Accepted:
            new_cfg = dlg.get_settings()
            self.manager.save_config(new_cfg)
            self.lang = self.manager.get_language()
            self.theme = self.manager.get_theme()
            self.apply_theme_and_lang()

    # === גרירת חלון ===
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos") and self.oldPos:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None
