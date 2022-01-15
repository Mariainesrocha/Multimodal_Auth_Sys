from PyQt5 import QtCore, QtGui, QtWidgets
from error_window import Ui_error_window
from voice_login import Ui_voice_login_window


class Ui_hand_login_window(object):
    def showErrorMessage(self): #error in hand login
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error_window()
        self.ui.setupUi(self.window)
        self.window.show()
            
    def openVoiceLogin(self, current_window): #if success in hand login 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_voice_login_window()
        self.ui.setupUi(self.window)
        self.window.show()    
        current_window.hide() ## TODO: CHANGED THIS
        
    def setupUi(self, hand_login_window):
        hand_login_window.setObjectName("hand_login_window")
        hand_login_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(hand_login_window)
        self.centralwidget.setObjectName("centralwidget")
        
        # btn
        self.btn_start = QtWidgets.QPushButton(self.centralwidget,  clicked=lambda: self.openVoiceLogin(hand_login_window))
        self.btn_start.setGeometry(QtCore.QRect(260, 490, 231, 51))
        self.btn_start.setObjectName("btn_start")
        
        #image
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 90, 691, 371))
        self.image.setObjectName("image")
        
        # text to user
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(30, 30, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        
        hand_login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hand_login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        hand_login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hand_login_window)
        self.statusbar.setObjectName("statusbar")
        hand_login_window.setStatusBar(self.statusbar)

        self.retranslateUi(hand_login_window)
        QtCore.QMetaObject.connectSlotsByName(hand_login_window)

    def retranslateUi(self, hand_login_window):
        _translate = QtCore.QCoreApplication.translate
        hand_login_window.setWindowTitle(_translate("hand_login_window", "Multimodal Authentication System - Hand"))
        self.btn_start.setText(_translate("hand_login_window", "Start Recording"))
        self.image.setText(_translate("hand_login_window", "TextLabel")) ## TODO: comentar qdo tiver imagem da camera a ser loaded


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hand_login_window = QtWidgets.QMainWindow()
    ui = Ui_hand_login_window()
    ui.setupUi(hand_login_window)
    hand_login_window.show()
    sys.exit(app.exec_())
