# Code is adapted from Codemy.com youtube PyQt5 channel


import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Front_Ui.ui", self)
        self.show()

#main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())

