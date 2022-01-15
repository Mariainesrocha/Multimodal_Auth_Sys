from PyQt5 import QtCore, QtGui, QtWidgets
from hand_register import Ui_hand_register_window
from hand_login import Ui_hand_login_window

class Ui_MainWindow(object):
    def openRegister(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_hand_register_window()
        self.ui.setupUi(self.window)
        self.window.show()
        
        ## Get username input
        username = self.user_name.text()
        self.ui.text.setText("Hello "+ username +"! Please put your hand in front of the camera.")
 
        MainWindow.hide() #closes this window
        
    def openLogin(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_hand_login_window()
        self.ui.setupUi(self.window)
        self.window.show()
        
        ## Get username input
        username = self.user_name.text()
        self.ui.text.setText("Welcome back "+ username +"! Show me your hand, please.")
        
        MainWindow.hide() #closes this window

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.register_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openRegister())
        self.register_btn.setGeometry(QtCore.QRect(430, 390, 301, 91))
        self.register_btn.setObjectName("register_btn")
        
        self.login_btn = QtWidgets.QPushButton(self.centralwidget,  clicked = lambda: self.openLogin())
        self.login_btn.setGeometry(QtCore.QRect(80, 390, 301, 91))
        self.login_btn.setObjectName("login_btn")
        
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(100, 240, 601, 31))
        self.user_name.setObjectName("user_name")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 371, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multimodal Authentication System"))
        self.register_btn.setText(_translate("MainWindow", "Register"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.user_name.setText(_translate("MainWindow", "Enter your name"))
        self.label.setText(_translate("MainWindow", "Welcome to our system"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
