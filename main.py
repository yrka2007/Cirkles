import sys
from random import randint, choice

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Круги')
        self.pushButton.clicked.connect(self.create_circle)
        self.circles = []

    def create_circle(self):
        r = randint(40, 300)
        x = randint(0, self.width()) - r // 2
        y = randint(0, self.height()) - r // 2
        color = choice(['black', 'red', 'blue', 'yellow', 'green', 'purple'])
        self.circles.append((x, y, r, color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        for el in self.circles:
            qp.setPen(QPen(QColor(el[3]), 4, Qt.SolidLine))
            qp.drawArc(el[0], el[1], el[2], el[2], 0, 360 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Circles()
    form.show()
    sys.exit(app.exec())
