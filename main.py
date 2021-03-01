  
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.flag = False
        self.qp = QPainter()
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            r, g, b = 255, 250, 57
            self.qp.begin(self)
            self.qp.setPen(QColor(r, g, b))
            self.qp.setBrush(QColor(r, g, b))
            self.qp.drawEllipse(*[random.randint(50, 400), random.randint(50, 400)], random.randint(70, 150), random.randint(70, 150))
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
