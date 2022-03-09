import os
import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import csv

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()
        self.show()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print(row, col, value, type(value))

    def open_sheet(self):
        self.check_change = False
        path = QFileDialog.getOpenFileNames(self, 'Open CSV', os.getenv('HOME'))
        print(path[0])
        if path[0] != '':
            with open(path[0][0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
            csv_file.close()
        self.check_change = True

class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        # self.form_widget.setCurrentCell(0, 0)
        # row, col = self.form_widget.currentRow(), self.form_widget.currentColumn()
        # print(row, col)
        self.form_widget.open_sheet()
        self.show()


app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())
