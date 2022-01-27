from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from hand_backend import *

current_window = None

class Ui_hand_register_window(object):
    def call_video(self,username):
        video(self,username,True)  
        current_window.hide()          

    def setupUi(self, hand_register_window):
        hand_register_window.setObjectName("hand_register_window")
        hand_register_window.resize(800, 600)
        hand_register_window.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/hand_wd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hand_register_window.setWindowIcon(icon)
        hand_register_window.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(hand_register_window)
        self.centralwidget.setObjectName("centralwidget")
        
        #image
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(60, 80, 691, 451))
        self.image.setObjectName("image")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        
        #text2user
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(40, 20, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        
        hand_register_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(hand_register_window)
        self.statusbar.setObjectName("statusbar")
        hand_register_window.setStatusBar(self.statusbar)

        self.retranslateUi(hand_register_window)
        QtCore.QMetaObject.connectSlotsByName(hand_register_window)
        global current_window
        current_window = hand_register_window

    def retranslateUi(self, hand_register_window):
        _translate = QtCore.QCoreApplication.translate
        hand_register_window.setWindowTitle(_translate("hand_register_window", "BioGuardian - Hand Register"))
        self.text.setText(_translate("hand_register_window", "Hello. Please put your hand in front of the camera to be registered."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hand_register_window = QtWidgets.QMainWindow()
    ui = Ui_hand_register_window()
    ui.setupUi(hand_register_window)
    hand_register_window.show()
    sys.exit(app.exec_())
