import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *


class Form(QMainWindow):
    def __init__(self, table):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.connection = sqlite3.connect("coffee.sqlite", timeout=10)
        cur = self.connection.cursor()
        self.cur = cur
        self.tableWidget = table
        self.pushButton.clicked.connect(self.add)
        titles = cur.execute("""SELECT name FROM coffee""").fetchall()
        self.connection.close()
        for i in titles:
            self.comboBox.addItem(i[0])

    def add(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection.cursor()
        id = self.cur.execute("SELECT MAX(id) FROM coffee").fetchone()[0] + 1
        self.cur.execute(f"""INSERT INTO coffee(id, name, degree, is_ground, taste, price, value) 
                                 VALUES({id}, '{self.lineEdit.text()}', '{self.lineEdit_2.text()}',
                                 '{self.comboBox.currentText()}', '{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}'
                                    , '{self.lineEdit_5.text()}')""").fetchall()
        self.connection.commit()
        req = "SELECT * FROM coffee"
        result = self.cur.execute(req).fetchall()
        cols = self.tableWidget.rowCount() + 1
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                cols)
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(
                i, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(
                i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(
                i, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(
                i, 6, QTableWidgetItem(str(row[6])))
        self.tableWidget.resizeColumnsToContents()
        self.connection.close()
        self.close()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.connection = sqlite3.connect("coffee.sqlite")
        cur = self.connection.cursor()
        self.cur = cur
        req = "SELECT * FROM coffee"
        result = cur.execute(req).fetchall()
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(
                i, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(
                i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(
                i, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(
                i, 6, QTableWidgetItem(str(row[6])))
        self.tableWidget.resizeColumnsToContents()
        self.pushButton.clicked.connect(self.check)
        self.connection.close()

    def check(self):
        global form
        form = Form(table=self.tableWidget)
        form.show()
        self.connection = sqlite3.connect("coffee.sqlite")
        cur = self.connection.cursor()
        req = "SELECT * FROM coffee"
        result = cur.execute(req).fetchall()
        cols = self.tableWidget.rowCount() + 1
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                cols)
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(
                i, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(
                i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(
                i, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(
                i, 6, QTableWidgetItem(str(row[6])))
        self.tableWidget.resizeColumnsToContents()
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
