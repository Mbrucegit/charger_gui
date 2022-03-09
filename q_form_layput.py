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
        # self.setLayout(qtw.QVBoxLayout())
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add Stuff/Widget
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont("Helvetica", 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # Add Rows to App
        form_layout.addRow(label_1)
        form_layout.addRow("First_Name", f_name)
        form_layout.addRow("Last_Name", l_name)
        form_layout.addRow(qtw.QPushButton("Press me!", clicked=lambda: press_it()))

        # Show the app
        self.show()

        def press_it():
            label_1.setText(f'you clicked the button, {f_name.text()}')

if __name__ == '__main__':
        app = qtw.QApplication(sys.argv)
        combo = MainWindow()
        sys.exit(app.exec_())
