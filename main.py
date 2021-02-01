import sqlite3
import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        query = QSqlQuery()
        query.exec(

            """
               SELECT * FROM coffee
                """
        )
        model = QSqlTableModel(self, db)
        model.setQuery(query)
        model.select()
        self.tableView.setModel(model)
        self.model = model
        self.query = query


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
