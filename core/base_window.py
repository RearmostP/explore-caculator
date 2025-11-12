from PyQt5 import QtWidgets, QtGui, QtCore
from core.app_manager import AppManager


class BaseWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.manager = AppManager.instance()
        self.lang = self.manager.get_language()
        self.theme = self.manager.get_theme()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def apply_theme_and_lang(self):
        """מעדכן שפה ועיצוב (להשתמש בכל חלון יורש)"""
        self.lang = self.manager.get_language()
        self.theme = self.manager.get_theme()

    def fade_transition(self, duration=400):
        """אנימציית פתיחה רכה (fade-in) לכל חלון"""
        self.anim = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(duration)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.anim.start()

    def return_to_main(self):
        """פותח מחדש את החלון הראשי באנימציה רכה"""
        import importlib
        main_module = importlib.import_module("windows.main_window")
        MainWindow = getattr(main_module, "MainWindow")

        self.main_window = MainWindow()
        self.main_window.setWindowOpacity(1.0)
        self.main_window.show()
        QtCore.QTimer.singleShot(50, lambda: self.fade_in(self.main_window))
        self.close()

    def fade_in(self, window):
        """אנימציית fade-in עדינה שלא גורמת לחלון להיעלם לגמרי"""
        window.setWindowOpacity(0.3)  # מתחיל מעט שקוף, לא לגמרי שקוף
        self.anim = QtCore.QPropertyAnimation(window, b"windowOpacity")
        self.anim.setDuration(400)
        self.anim.setStartValue(0.3)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutQuad)  # ← כאן חסר הסוגר והערך
        self.anim.start()

