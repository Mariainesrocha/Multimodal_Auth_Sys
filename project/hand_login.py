from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from hand_backend import *

current_window = None

class Ui_hand_login_window(object):
    def call_video(self,username):
        video(self,username)  
        current_window.hide()
    
    def setupUi(self, hand_login_window):
        hand_login_window.setObjectName("hand_login_window")
        hand_login_window.resize(800, 600)
        hand_login_window.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/hand_wd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hand_login_window.setWindowIcon(icon)
        hand_login_window.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(hand_login_window)
        self.centralwidget.setObjectName("centralwidget")
        
        #image
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 80, 781, 491))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        
        # text2user
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
        self.statusbar = QtWidgets.QStatusBar(hand_login_window)
        self.statusbar.setObjectName("statusbar")
        hand_login_window.setStatusBar(self.statusbar)

        self.retranslateUi(hand_login_window)
        QtCore.QMetaObject.connectSlotsByName(hand_login_window)
        global current_window
        current_window = hand_login_window

    def retranslateUi(self, hand_login_window):
        _translate = QtCore.QCoreApplication.translate
        hand_login_window.setWindowTitle(_translate("hand_login_window", "BioGuardian - Hand Login"))
        self.text.setText(_translate("hand_login_window", "Welcome back. Please show me your beautiful hand."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hand_login_window = QtWidgets.QMainWindow()
    ui = Ui_hand_login_window()
    ui.setupUi(hand_login_window)
    hand_login_window.show()
    sys.exit(app.exec_())
