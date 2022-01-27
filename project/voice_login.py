from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from voice_backend import *
import os
current_user = None

class Ui_voice_login_window(object):
    def set_user(self,username):
        global current_user
        current_user = username
        print(current_user)

    def process_voice(self,current_window):
        audio(current_user) 
        if compare(current_user, current_window):
            showSuccessMsg(self, "User authenticated with success!")
        else:
            showErrorMsg(self, "Something went wrong!\nPlease try again.")
        
        ## delete login audio
        file_ = './audios/'+current_user+'.wav'
        if os.path.exists(file_):
            os.remove(file_)
        current_window.hide()
       

    def setupUi(self, voice_login_window):
        voice_login_window.setObjectName("voice_login_window")
        voice_login_window.resize(800, 600)
        voice_login_window.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/voice_wd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        voice_login_window.setWindowIcon(icon)
        voice_login_window.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(voice_login_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 751, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setObjectName("gif")
        self.gif.setGeometry(QtCore.QRect(150, 80, 501, 371))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("images/micro1.gif"))
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.movie = QMovie("images/micro1.gif")
        self.gif.setMovie(self.movie)
        self.movie.start()

        ## record_btn
        self.record_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.process_voice(voice_login_window))
        self.record_btn.setGeometry(QtCore.QRect(250, 470, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.record_btn.setFont(font)
        self.record_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"border-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/rec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record_btn.setIcon(icon1)
        self.record_btn.setIconSize(QtCore.QSize(40, 40))
        self.record_btn.setObjectName("record_btn")
        
        voice_login_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(voice_login_window)
        self.statusbar.setObjectName("statusbar")
        voice_login_window.setStatusBar(self.statusbar)

        self.retranslateUi(voice_login_window)
        QtCore.QMetaObject.connectSlotsByName(voice_login_window)

    def retranslateUi(self, voice_login_window):
        _translate = QtCore.QCoreApplication.translate
        voice_login_window.setWindowTitle(_translate("voice_login_window", "BioGuardian - Voice Login"))
        self.label.setText(_translate("voice_login_window", "Please say something kind to our guardian."))
        self.record_btn.setText(_translate("voice_login_window", "Start Recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voice_login_window = QtWidgets.QMainWindow()
    ui = Ui_voice_login_window()
    ui.setupUi(voice_login_window)
    voice_login_window.show()
    sys.exit(app.exec_())
