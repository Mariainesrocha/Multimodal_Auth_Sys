
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_msg_success(object):
    def setupUi(self, msg_success):
        msg_success.setObjectName("msg_success")
        msg_success.resize(523, 337)
        msg_success.setMaximumSize(QtCore.QSize(523, 337))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_success.setWindowIcon(icon)
        msg_success.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")

        self.register_success_msg = QtWidgets.QLabel(msg_success)
        self.register_success_msg.setGeometry(QtCore.QRect(30, 40, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(11)
        self.register_success_msg.setFont(font)
        self.register_success_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.register_success_msg.setObjectName("register_success_msg")
        
        self.label = QtWidgets.QLabel(msg_success)
        self.label.setGeometry(QtCore.QRect(160, 160, 191, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/lock2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(msg_success)
        QtCore.QMetaObject.connectSlotsByName(msg_success)

    def retranslateUi(self, msg_success):
        _translate = QtCore.QCoreApplication.translate
        msg_success.setWindowTitle(_translate("msg_success", "Success Message"))
        msg_success.setToolTip(_translate("msg_success", "authentication success"))
        self.register_success_msg.setText(_translate("msg_success", "Message!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    msg_success = QtWidgets.QDialog()
    ui = Ui_msg_success()
    ui.setupUi(msg_success)
    msg_success.show()
    sys.exit(app.exec_())
