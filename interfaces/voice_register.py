from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from error_window import Ui_error_window
from registered_message import Ui_register_success

class Ui_voice_register_window(object):
    def showErrorMessage(self): #error in voice register
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error_window()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def showRegisterMsg(self):  # registered successfully
        self.window = QtWidgets.QDialog()
        self.ui = Ui_register_success()
        self.ui.setupUi(self.window)
        Ui_voice_register_window.hide()
    
    # Start Animation
    def startAnimation(self):
        self.movie.start()
          
    def setupUi(self, voice_register_window):
        voice_register_window.setObjectName("voice_register_window")
        voice_register_window.resize(800, 600)
        voice_register_window.setMinimumSize(QtCore.QSize(800, 600))
        voice_register_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(voice_register_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 471, 61))
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
        self.record_btn.setGeometry(QtCore.QRect(110, 450, 241, 71))
        self.record_btn.setObjectName("record_btn")
        
        #btn stop
        self.stop_record_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_record_btn.setGeometry(QtCore.QRect(430, 450, 241, 71))
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
        
        
        voice_register_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(voice_register_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        voice_register_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(voice_register_window)
        self.statusbar.setObjectName("statusbar")
        voice_register_window.setStatusBar(self.statusbar)

        self.retranslateUi(voice_register_window)
        QtCore.QMetaObject.connectSlotsByName(voice_register_window)

    def retranslateUi(self, voice_register_window):
        _translate = QtCore.QCoreApplication.translate
        voice_register_window.setWindowTitle(_translate("voice_register_window", "Multimodal Authentication System - Voice"))
        self.label.setText(_translate("voice_register_window", "Please speak to the microphone."))
        self.record_btn.setText(_translate("voice_register_window", "Start Recording"))
        self.image_label.setText(_translate("voice_register_window", "TextLabel"))
        self.stop_record_btn.setText(_translate("voice_register_window", "Stop Recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voice_register_window = QtWidgets.QMainWindow()
    ui = Ui_voice_register_window()
    ui.setupUi(voice_register_window)
    voice_register_window.show()
    sys.exit(app.exec_())
