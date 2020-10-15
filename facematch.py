import os
import threading

from PyQt5 import QtCore,QtGui,QtWidgets



class FACE(threading.Thread, QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        threading.Thread.__init__(self)

        self.setFixedSize(800,600)
        self.setStyleSheet("background-color:#000000")
        self.label_animation = QtWidgets.QLabel(self)

        self.movie = QtGui.QMovie('FACE.GIF')
        self.label_animation.setMovie(self.movie)
        timer = QtCore.QTimer(self)

        self.startimation()
        timer.singleShot(6000,self.stopimation)

        self.show()

    def startimation(self):
        self.movie.start()

    def stopimation(self):
        self.movie.stop()
        self.close()