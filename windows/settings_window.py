from PyQt5 import QtWidgets

class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent, current_lang, current_theme):
        super().__init__(parent)
        self.setWindowTitle("הגדרות")
        self.resize(280, 200)
        layout = QtWidgets.QVBoxLayout(self)

        # שפה
        layout.addWidget(QtWidgets.QLabel("בחר שפה:"))
        self.lang_combo = QtWidgets.QComboBox()
        self.lang_combo.addItem("עברית", "he")
        self.lang_combo.addItem("English", "en")
        self.lang_combo.addItem("Русский", "ru")
        self.lang_combo.setCurrentIndex(self.lang_combo.findData(current_lang))
        layout.addWidget(self.lang_combo)

        # עיצוב
        layout.addWidget(QtWidgets.QLabel("בחר עיצוב:"))
        self.theme_combo = QtWidgets.QComboBox()
        self.theme_combo.addItem("כהה", "dark")
        self.theme_combo.addItem("בהיר", "light")
        self.theme_combo.setCurrentIndex(self.theme_combo.findData(current_theme))
        layout.addWidget(self.theme_combo)

        # כפתורים
        buttons = QtWidgets.QHBoxLayout()
        ok_btn = QtWidgets.QPushButton("אישור")
        cancel_btn = QtWidgets.QPushButton("ביטול")
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        buttons.addStretch()
        buttons.addWidget(cancel_btn)
        buttons.addWidget(ok_btn)
        layout.addLayout(buttons)

    def get_settings(self):
        """מחזיר מילון עם בחירת המשתמש"""
        return {
            "language": self.lang_combo.currentData(),
            "theme": self.theme_combo.currentData()
        }
