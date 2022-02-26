import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Front_Ui.ui", self)
        self.show()

#main
app = QApplication(sys.argv)
mainwindow = MainWindow()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
