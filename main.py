import random
import sys

from PyQt5.Qt import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Draw(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.figure = None

    def initUI(self):
        self.setWindowTitle('Супрематизм')
        self.setGeometry(200, 200, 700, 700)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.figure == 1:
            a = random.randint(5, self.width() // 4)
            qp.setBrush(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)))
            qp.drawEllipse(self.x - a, self.y - a, a * 2, a * 2)

        if self.figure == 2:
            a = random.randint(5, self.width() // 4)
            qp.setBrush(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)))
            qp.drawRect(self.x - a, self.y - a, a * 2, a * 2)

        if self.figure == 3:
            a = random.randint(5, self.width() // 4)
            qp.setBrush(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)))
            qp.drawPolygon(QPointF(self.x, self.y - 2 * a),
                           QPointF(self.x + int(3 ** 0.5 * a), self.y + a),
                           QPointF(self.x - int(3 ** 0.5 * a), self.y + a))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.figure = 1
            self.update()
        if event.button() == Qt.RightButton:
            self.figure = 2
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figure = 3
            self.update()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
