from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error_window(object):
    
    def setupUi(self, error_window):
        error_window.setObjectName("error_window")
        error_window.resize(400, 300)
        error_window.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        icon = QtGui.QIcon()
        error_window.setFont(font)
        icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error_window.setWindowIcon(icon)
        error_window.setStyleSheet("background-color: rgb(35, 35, 35); \nborder-color: rgb(42, 42, 42);\ncolor: rgb(255, 255, 255);")
        
        self.error_msg = QtWidgets.QLabel(error_window)
        self.error_msg.setGeometry(QtCore.QRect(50, 50, 291, 131))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_msg.setFont(font)
        self.error_msg.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.error_msg.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")

        self.label = QtWidgets.QLabel(error_window)
        self.label.setGeometry(QtCore.QRect(150, 140, 80, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/error_icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(error_window)        
        QtCore.QMetaObject.connectSlotsByName(error_window)

    def retranslateUi(self, error_window):
        _translate = QtCore.QCoreApplication.translate
        error_window.setWindowTitle(_translate("error_window", "Attention Error"))
        self.error_msg.setText(_translate("error_window", "Error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_window = QtWidgets.QDialog()
    ui = Ui_error_window()
    ui.setupUi(error_window)
    error_window.show()
    sys.exit(app.exec_())
