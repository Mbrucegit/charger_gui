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
        self.my_label = qtw.QLabel("Type something into the box below")
        # Change the font size of label
        self.my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(self.my_label)

        # Create a Textbox #QDoubleSpinBox #QSpinbox
        self.my_text = qtw.QTextEdit(self,
                                #plainText="This is text"
                                #Html
                                acceptRichText=True,
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText="Hello World",
                                readOnly=False,
                                     )
        # Change font size

        # Add item to the combo
        self.layout().addWidget(self.my_text)

        # Create a button
        self.my_btn = qtw.QPushButton("Press Me!")
        self.my_btn.clicked.connect(self.press_it)
        self.layout().addWidget(self.my_btn)

        self.show()

    def press_it(self):
        self.my_label.setText(f'You picked {self.my_text.toPlainText()}')
        self.my_text.setPlainText('You clicked the button')


if __name__ == '__main__':
        app = qtw.QApplication(sys.argv)
        combo = MainWindow()
        sys.exit(app.exec_())
