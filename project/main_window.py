from PyQt5 import QtCore, QtGui, QtWidgets
from hand_register import Ui_hand_register_window
from hand_login import Ui_hand_login_window
from pymongo import MongoClient
from error_window import Ui_error_window
import os
from audios_encryption import FernetKey

def findVoice(username):
    return os.path.exists('./audios/'+username+'_regist.wav')

def deleteVoice(username):
    regist = './audios/'+username+'_regist.wav'
    login = './audios/'+username+'.wav'
    if os.path.exists(regist):
        os.remove(regist)
    if os.path.exists(login):
        os.remove(login)

def exists_user(username, register=False):
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["biometry"]
    mycol = mydb["user_Data"]
    count = mycol.count_documents({"user": username})
    if count > 0:   #User already exists
        mydoc = mycol.find({"user": username},{"_id":0,"hand_metric":1})
        hand_metric = mydoc[0]["hand_metric"]
        if hand_metric == 0 or not findVoice(username):    #regist incomplete -> delete user -> free to use
            mycol.delete_many({"user": username})
            deleteVoice(username)
            return exists_user(username,register)
        return True 
    else:   #User does not exist
        if findVoice(username): #if not exist -> it cannot exist voice files with his name
            deleteVoice(username)
        if register:
            fk = FernetKey()
            mycol.insert_one({"user": username, "hand_metric": 0, "fernet": fk})
        return False # Partial register successful

class Ui_MainWindow(object):
    def showErrorMessage(self,msg):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error_window()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.error_msg.setText(msg)
        
    def openWindow(self, attempt_regist=False):        
        ## Get username input
        username = self.user_name.text()

        #Remove white space from username
        username = username.replace(" ", "")
        if username == "":
            self.showErrorMessage("Invalid username!")
            return
        
        status = exists_user(username,attempt_regist)
        self.window =  QtWidgets.QMainWindow()
        if attempt_regist: ##register
            if status:
                msg = "User already exists!"
                self.showErrorMessage(msg)  
            else:
                self.ui = Ui_hand_register_window()
                self.ui.setupUi(self.window)
                self.ui.text.setText("Hello "+ username +"! Please put your hand in front of the camera.")
                MainWindow.hide() #closes this window
                self.window.show()
                self.ui.call_video(username) #starts video
        else: ##login
            if status:
                self.ui = Ui_hand_login_window()
                self.ui.setupUi(self.window)
                self.ui.text.setText("Welcome back "+ username +"! Show me your hand, please.")
                MainWindow.hide() #closes this window
                self.window.show()
                self.ui.call_video(username) #starts video
            else:
                msg = "User does not exist!"
                self.showErrorMessage(msg)            

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);\n"
        "border-color: rgb(42, 42, 42);\n"
        "color: rgb(255, 255, 255);\n"
        "alternate-background-color: rgb(255, 255, 255);\n"
        "alternate-background-color: rgb(85, 170, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
         
        self.register_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow(True))
        self.register_btn.setGeometry(QtCore.QRect(410, 390, 301, 91))
        self.register_btn.setObjectName("register_btn")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"border-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_btn.setIcon(icon1)
        self.register_btn.setIconSize(QtCore.QSize(40, 30))
        

        self.login_btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow(False))
        self.login_btn.setGeometry(QtCore.QRect(80, 390, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"border-color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/login1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(40, 40))
        self.login_btn.setObjectName("login_btn")

        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(100, 260, 601, 41))
        self.user_name.setText("")
        self.user_name.setObjectName("user_name")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 401, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 100, 161, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/main_icon.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
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
        self.user_name.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.label.setText(_translate("MainWindow", "Welcome to BioGuardian")) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
