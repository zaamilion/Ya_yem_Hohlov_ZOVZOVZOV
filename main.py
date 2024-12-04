import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []  # Список для хранения окружностей
        self.pushButton.clicked.connect(self.add_circle)  # Подключение кнопки

    def add_circle(self):
        # Генерация случайного диаметра и позиции
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()  # Обновление окна для перерисовки

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  # Установка желтого цвета
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)  # Рисуем окружности


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec_())
