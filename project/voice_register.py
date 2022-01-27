from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from voice_backend import *
current_window = None
current_user = None

class Ui_voice_register_window(object):    
    def set_user(self,username):
        global current_user
        current_user = username
        print(current_user)

    def process_voice(self,cw):
        audio(current_user+"_regist",current_user,True) 
        cw.hide()
        showSuccessMsg(cw, "Your register is complete! Please try to login.")
        
    # Start Animation
    def startAnimation(self):
        self.gif.start()
          
    def setupUi(self, voice_register_window):
        voice_register_window.setObjectName("voice_register_window")
        voice_register_window.resize(800, 600)
        voice_register_window.setMinimumSize(QtCore.QSize(800, 600))
        voice_register_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(voice_register_window)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/voice_wd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        voice_register_window.setWindowIcon(icon)
        voice_register_window.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(42, 42, 42);\n"
"color: rgb(255, 255, 255);")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 751, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        #btn_start
        self.record_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.process_voice(voice_register_window))
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
       
        #gif
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setObjectName("gif")
        self.gif.setGeometry(QtCore.QRect(150, 80, 501, 371))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("images/micro1.gif"))
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.movie = QMovie("images/micro1.gif")
        self.gif.setMovie(self.movie)
        self.movie.start()
        
        voice_register_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(voice_register_window)
        self.statusbar.setObjectName("statusbar")
        voice_register_window.setStatusBar(self.statusbar)

        self.retranslateUi(voice_register_window)
        QtCore.QMetaObject.connectSlotsByName(voice_register_window)
        global current_window
        current_window = voice_register_window

    def retranslateUi(self, voice_register_window):
        _translate = QtCore.QCoreApplication.translate
        voice_register_window.setWindowTitle(_translate("voice_register_window", "BioGuardian - Voice Register"))
        self.label.setText(_translate("voice_register_window", "Please speak to the microphone to register your voice."))
        self.record_btn.setText(_translate("voice_register_window", "Start Recording"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voice_register_window = QtWidgets.QMainWindow()
    ui = Ui_voice_register_window()
    ui.setupUi(voice_register_window)
    voice_register_window.show()
    sys.exit(app.exec_())