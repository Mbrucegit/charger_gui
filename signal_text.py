import sys
from PyQt5 import uic
import PyQt5.QtWidgets as qtw


class SignalWindow(qtw.QMainWindow):
    def __init__(self):
        super(SignalWindow, self).__init__()
        self.setWindowTitle("Signal-Plot")

        # Load the UI file
        uic.loadUi('Signal_text.ui', self)

        # define the widget
        self.my_label= self.findChild(qtw.QLabel, 'my_label')

        self.my_edit = self.findChild(qtw.QLineEdit, 'my_edit')

        pushButton = self.findChild(qtw.QPushButton, 'pushButton')

        # Button action
        pushButton.clicked.connect(self.clicker)

        self.textchanged()

        self.show()

    def textchanged(self):
        self.my_label.changeEvent(self, )

    def clicker(self):
        self.my_label.setText(f'You picked {self.my_edit.text()}')

        # show the app


# initialize the App
app = qtw.QApplication(sys.argv)
signalWindow = SignalWindow()
sys.exit(app.exec_())
