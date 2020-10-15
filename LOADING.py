import sys 
import os
import threading

from PyQt5 import QtCore,QtGui,QtWidgets

class ls(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(508,319)
        self.setStyleSheet("background-color:#000000")

        self.label_animation =QtWidgets.QLabel(self)

        self.movie = QtGui.QMovie('EDITIOR MODE.gif')
        self.label_animation.setMovie(self.movie)

        timer = QtCore.QTimer(self)

        self.startAnimation()
        timer.singleShot(4000,self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class ad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        
        self.loading_screen = ls()


app = QtWidgets.QApplication(sys.argv)


demo =ad()

app.exit(app.exec_())