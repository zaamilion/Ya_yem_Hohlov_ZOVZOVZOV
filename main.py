import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 400, 300)

        # Создание кнопки
        self.pushButton = QtWidgets.QPushButton("Добавить окружность", self)
        self.pushButton.setGeometry(150, 250, 100, 30)
        self.pushButton.clicked.connect(self.add_circle)  # Подключение кнопки

        self.circles = []  # Список для хранения окружностей

    def add_circle(self):
        # Генерация случайного диаметра и позиции
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )  # Случайный цвет
        self.circles.append((x, y, diameter, color))
        self.update()  # Обновление окна для перерисовки

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)  # Установка случайного цвета
            painter.drawEllipse(x, y, diameter, diameter)  # Рисуем окружности


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec_())
