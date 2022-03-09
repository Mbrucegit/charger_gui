import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys


class MainWindow(qtw.QWidget):
    def __init__(self):
        # Inherit parent class
        super().__init__()
        # Add a title
        self.setWindowTitle('Hello World!!')

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a Label
        self.my_label = qtw.QLabel("Pick something from the list")
        # Change the font size of label
        self.my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(self.my_label)

        # Create a combo box
        self.my_combo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)
        # Add item to the combo
        self.my_combo.addItem('Peperonix', 1)
        self.my_combo.addItem('Cheese', 2)
        self.my_combo.addItem('Apple', 3)
        self.my_combo.addItem('Beef', 4)
        self.my_combo.addItems(['1', '2', '3'])
        self.my_combo.insertItems(3, ['Third', 'One'])
        self.layout().addWidget(self.my_combo)

        # Create a button
        self.my_btn = qtw.QPushButton("Press Me!")
        self.my_btn.clicked.connect(self.press_it)
        self.layout().addWidget(self.my_btn)

        self.show()

    def press_it(self):
        self.my_label.setText(f'You picked {self.my_combo.currentText()}')


if __name__ == '__main__':
        app = qtw.QApplication(sys.argv)
        combo = MainWindow()
        sys.exit(app.exec_())




