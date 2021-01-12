import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtGui import QPixmap, QPainter, QColor
from random import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.do_paint = True

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        try:
            qp.setBrush(QColor('Yellow'))
            a = randint(1, 100)
            qp.drawEllipse(200, 200, a, a)
        except ValueError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
