import sys 
import os
import threading

from PyQt5 import QtCore,QtGui,QtWidgets

class WH(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800,600)
        self.setStyleSheet("background-color:#000000")

        self.label_animation =QtWidgets.QLabel(self)

        self.movie = QtGui.QMovie('5 (1).gif')
        self.label_animation.setMovie(self.movie)

        timer = QtCore.QTimer(self)

        self.startAnimation()
        timer.singleShot(3000,self.stopAnimation)

        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class ad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        
        self.loading_screen = WH()


app = QtWidgets.QApplication(sys.argv)


demo =ad()

app.exit(app.exec_())