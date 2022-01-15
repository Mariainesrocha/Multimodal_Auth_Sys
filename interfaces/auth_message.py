from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auth_success(object):
    def setupUi(self, auth_success):
        auth_success.setObjectName("auth_success")
        auth_success.resize(523, 337)
        
        self.register_success_msg = QtWidgets.QLabel(auth_success)
        self.register_success_msg.setGeometry(QtCore.QRect(30, 70, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(11)
        self.register_success_msg.setFont(font)
        self.register_success_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.register_success_msg.setObjectName("register_success_msg")
        
        self.name_regist = QtWidgets.QLabel(auth_success)
        self.name_regist.setGeometry(QtCore.QRect(130, 170, 291, 111))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_regist.setFont(font)
        self.name_regist.setAlignment(QtCore.Qt.AlignCenter)
        self.name_regist.setObjectName("name_regist")

        self.retranslateUi(auth_success)
        QtCore.QMetaObject.connectSlotsByName(auth_success)

    def retranslateUi(self, auth_success):
        _translate = QtCore.QCoreApplication.translate
        auth_success.setWindowTitle(_translate("auth_success", "Register Message"))
        self.register_success_msg.setText(_translate("auth_success", "You were registed successfully with the username:"))
        self.name_regist.setText(_translate("auth_success", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auth_success = QtWidgets.QDialog()
    ui = Ui_auth_success()
    ui.setupUi(auth_success)
    auth_success.show()
    sys.exit(app.exec_())
