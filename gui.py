import os
import threading

from PyQt5 import QtCore,QtGui,QtWidgets


class GUI(threading.Thread, QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        threading.Thread.__init__(self)

        self.setFixedSize(1366,768)
        self.setStyleSheet("background-color:#000000")
        self.label_animation = QtWidgets.QLabel(self)

        self.movie = QtGui.QMovie('5 (3).GIF')
        self.label_animation.setMovie(self.movie)

        timer = QtCore.QTimer(self)

        self.startnimation()
        timer.singleShot(4000,self.stopnimation)

        self.show()

    def startnimation(self):
        self.movie.start()

    def stopnimation(self):
        self.movie.stop()
        self.close()

