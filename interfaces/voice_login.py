from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from error_window import Ui_error_window
from auth_message import Ui_auth_success


class Ui_voice_login_window(object):
    def showErrorMessage(self): #error in voice login
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error_window()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def showAuthMsg(self, current_window): # authenticated successfully
        self.window = QtWidgets.QDialog()
        self.ui = Ui_auth_success()
        self.ui.setupUi(self.window)
        self.window.show()    
        current_window.hide()

    # Start Animation
    def startAnimation(self):
        self.movie.start()
        
    def setupUi(self, voice_login_window):
        voice_login_window.setObjectName("voice_login_window")
        voice_login_window.resize(800, 600)
        voice_login_window.setMinimumSize(QtCore.QSize(800, 600))
        voice_login_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(voice_login_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 471, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        #btn_start
        self.record_btn = QtWidgets.QPushButton(self.centralwidget)
        self.record_btn.setGeometry(QtCore.QRect(160, 450, 241, 71))
        self.record_btn.setObjectName("record_btn")
        
        #btn stop
        self.stop_record_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_record_btn.setGeometry(QtCore.QRect(410, 450, 241, 71))
        self.stop_record_btn.setObjectName("stop_record_btn")
        
        #gif        
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(340, 440, 624, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setToolTipDuration(0)
        self.image_label.setObjectName("image_label")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 100, 431, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setObjectName("gif")
        self.verticalLayout.addWidget(self.gif)
        self.movie = QMovie("./images/micro1.gif")
        self.gif.setMovie(self.movie)
        self.startAnimation()
        
        
        voice_login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(voice_login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        voice_login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(voice_login_window)
        self.statusbar.setObjectName("statusbar")
        voice_login_window.setStatusBar(self.statusbar)

        self.retranslateUi(voice_login_window)
        QtCore.QMetaObject.connectSlotsByName(voice_login_window)

    def retranslateUi(self, voice_login_window):
        _translate = QtCore.QCoreApplication.translate
        voice_login_window.setWindowTitle(_translate("voice_login_window", "Multimodal Authentication System - Voice"))
        self.label.setText(_translate("voice_login_window", "Show me your beautiful voice, please."))
        self.record_btn.setText(_translate("voice_login_window", "Start Recording"))
        self.image_label.setText(_translate("voice_login_window", "TextLabel"))
        self.stop_record_btn.setText(_translate("voice_login_window", "Stop Recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voice_login_window = QtWidgets.QMainWindow()
    ui = Ui_voice_login_window()
    ui.setupUi(voice_login_window)
    voice_login_window.show()
    sys.exit(app.exec_())
