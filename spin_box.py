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

        # Create a combo box  #QDoubleSpinBox #QSpinbox
        self.my_spin = qtw.QDoubleSpinBox(self,
                                 value=10,
                                 maximum=100,
                                 minimum=0,
                                 singleStep=5,
                                 prefix="Your order is #",
                                 suffix=" Order")
        # Change font size

        # Add item to the combo
        self.layout().addWidget(self.my_spin)

        # Create a button
        self.my_btn = qtw.QPushButton("Press Me!")
        self.my_btn.clicked.connect(self.press_it)
        self.layout().addWidget(self.my_btn)

        self.show()

    def press_it(self):
        self.my_label.setText(f'You picked {self.my_spin.value()}')


if __name__ == '__main__':
        app = qtw.QApplication(sys.argv)
        combo = MainWindow()
        sys.exit(app.exec_())
