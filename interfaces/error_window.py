from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error_window(object):
    
    def setupUi(self, error_window):
        error_window.setObjectName("error_window")
        error_window.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        error_window.setFont(font)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(error_window)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.error_msg = QtWidgets.QLabel(error_window)
        self.error_msg.setGeometry(QtCore.QRect(65, 90, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error_msg.setFont(font)
        self.error_msg.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")

        self.retranslateUi(error_window)
        
        self.buttonBox.accepted.connect(error_window.accept) # type: ignore
        self.buttonBox.rejected.connect(error_window.reject) # type: ignore
        
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
