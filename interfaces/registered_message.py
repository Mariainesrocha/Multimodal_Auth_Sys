from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_success(object):
    
    def setupUi(self, register_success):
        register_success.setObjectName("register_success")
        register_success.resize(523, 337)
    
        self.register_success_msg = QtWidgets.QLabel(register_success)
        self.register_success_msg.setGeometry(QtCore.QRect(20, 90, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(11)
        self.register_success_msg.setFont(font)
        self.register_success_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.register_success_msg.setObjectName("register_success_msg")
    
        self.name_regist = QtWidgets.QLabel(register_success)
        self.name_regist.setGeometry(QtCore.QRect(100, 190, 291, 111))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_regist.setFont(font)
        self.name_regist.setAlignment(QtCore.Qt.AlignCenter)
        self.name_regist.setObjectName("name_regist")

        self.retranslateUi(register_success)
        QtCore.QMetaObject.connectSlotsByName(register_success)

    def retranslateUi(self, register_success):
        _translate = QtCore.QCoreApplication.translate
        register_success.setWindowTitle(_translate("register_success", "Register Message"))
        self.register_success_msg.setText(_translate("register_success", "You were registered successfully with the username:"))
        self.name_regist.setText(_translate("register_success", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_success = QtWidgets.QDialog()
    ui = Ui_register_success()
    ui.setupUi(register_success)
    register_success.show()
    sys.exit(app.exec_())
