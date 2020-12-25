import sys,numpy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import cv2 as cv
import pyautogui,webbrowser,pyperclip


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.win_width = 340
        self.win_height = 200
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle('QR SCANNER')
        self.begin = QtCore.QPoint()
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0
        self.search_browser=''
        self.end = QtCore.QPoint()
         
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.x1,self.y1=pyautogui.position()

        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.x2,self.y2=pyautogui.position()
        self.end = event.pos()
        self.update()
    def onChanged(self, text):
        temp_text = f'Internet browser changed to {text}. \nIdle...'
        self.notificationText.setText(temp_text)
        self.update_notif()
        self.search_browser = self.combo.currentText()
    
  

    def mouseReleaseEvent(self, event):
        self.close()

        img = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2),include_layered_windows=False)
        

        im = numpy.array(img)

       
        det = cv.QRCodeDetector()
        retval, points, straight_qrcode = det.detectAndDecode(im)



        print(retval)
        """
        img.save('capture.png')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        
        for_showing_ccaptured_image
        cv2.imshow('Captured Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """
        pyperclip.copy(retval)
        if retval[-3:] == 'com' or retval[:3]=='www':
            self.openSite(retval)
            print("opensite")
        elif retval == '' or retval == ' ':
            print("Invalid QR CODE")
        else:
            self.google(retval)
            print("google")
            

    def openSite(self,url):
        webbrowser.open(url, new=1)

    def google(self, img_str):
        
        url = "https://www.google.com/search?q={}".format(img_str)
        webbrowser.open(url, new=1)

        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
