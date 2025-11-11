from PyQt5 import QtCore, QtGui, QtWidgets


class ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(90, 50, 150, 90))
        font = QtGui.QFont()
        font.setFamily("Fredoka-Regular")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Fredoka-Regular\";")
        self.main_label.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.main_label.setObjectName("main_label")
        self.creat_explore = QtWidgets.QPushButton(self.centralwidget)
        self.creat_explore.setGeometry(QtCore.QRect(220, 200, 121, 61))
        self.creat_explore.setStyleSheet("color:rgb(173, 179, 200)\n"
"")
        self.creat_explore.setObjectName("creat_explore")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(110, 300, 121, 61))
        self.settings.setStyleSheet("color:rgb(173, 179, 200)\n"
"")
        self.settings.setObjectName("settings")
        self.see_explores = QtWidgets.QPushButton(self.centralwidget)
        self.see_explores.setGeometry(QtCore.QRect(30, 200, 121, 61))
        self.see_explores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.see_explores.setStyleSheet("color:rgb(173, 179, 200)\n"
"")
        self.see_explores.setObjectName("see_explores")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "מחשב הוצאות"))
        self.creat_explore.setText(_translate("MainWindow", "יצירה רשימה חדשה"))
        self.settings.setText(_translate("MainWindow", "הגדרות"))
        self.see_explores.setText(_translate("MainWindow", "צפייה ברשימות"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
