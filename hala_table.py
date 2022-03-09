import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('tableUI.ui', self)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.loaddata()

    def loaddata(self):
        people = [{"name": "John", "age": 45, "address": "New York"},
                  {"name": "Jack", "age": 40, "address": "Chicago"},
                  {"name": "Tom", "age": 30, "address": "SFO"}]
        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["age"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["address"]))
            row += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(450)
    widget.setFixedWidth(620)
    widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")