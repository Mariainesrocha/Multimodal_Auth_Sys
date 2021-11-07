import sys
import cv2
import imutils

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

from demoUI import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)

        self.ui.verticalSlider.valueChanged.connect(self.set_brightness)
        self.ui.verticalSlider_2.valueChanged.connect(self.set_contrast)
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.pushButton_2.clicked.connect(self.saveFrame)
        

    def viewCam(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        #self.ui.image_label.setPixmap(QPixmap.fromImage(qImg).scaled(self.width(),self.height()))
        #self.ui.image_label.setPixmap(QPixmap.fromImage(qImg).scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        #self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def set_brightness(self, value):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def set_contrast(self, value):
        self.cap.set(cv2.CAP_PROP_CONTRAST, value)    
    
    def saveFrame(self):
        ret, image = self.cap.read()
        cv2.imwrite('frame.jpg', image)
        print("Frame Saved!")

    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            self.ui.control_bt.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())