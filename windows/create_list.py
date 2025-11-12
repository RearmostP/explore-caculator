from PyQt5 import QtWidgets, QtGui, QtCore
from core.base_window import BaseWindow


class CreateListWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        # === הגדרות בסיס ===
        self.setWindowTitle("יצירת רשימה חדשה")
        self.resize(400, 450)

        # === רקע ===
        self.bg = QtWidgets.QFrame(self)
        self.bg.setGeometry(5, 5, 390, 440)

        # === כפתור חזרה ===
        self.back_btn = QtWidgets.QPushButton("←", self.bg)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.back_btn.setStyleSheet("""
            QPushButton {
                color: #ccc;
                background-color: transparent;
                border: none;
                font: bold 18pt 'Segoe UI';
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.1);
            }
        """)
        self.back_btn.clicked.connect(self.return_to_main)

        # === כותרת ===
        self.title = QtWidgets.QLabel("יצירת רשימה חדשה", self.bg)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setGeometry(QtCore.QRect(50, 60, 300, 60))
        self.title.setStyleSheet("font: bold 16pt 'Segoe UI'; color: white;")

        # === עיצוב ראשוני ===
        self.apply_theme_and_lang()
        self.fade_transition()

    def return_to_main(self):
        """חזרה לחלון הראשי"""
        import importlib
        main_module = importlib.import_module("windows.main_window")
        MainWindow = getattr(main_module, "MainWindow")

        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
