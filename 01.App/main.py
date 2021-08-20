import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from devs import *


# Основной класс отвечающий за первое окно
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Подключаем кнопки
        self.ui.pushButton.clicked.connect(self.first)
        self.ui.pushButton_2.clicked.connect(self.second)
        self.ui.pushButton_3.clicked.connect(self.third)
        self.ui.pushButton_4.clicked.connect(self.next)

    # Програмируем все кнопки
    # Кнопка "Хлеб"
    def third(self):
        # Блокаем 3-ю кнопку
        self.ui.pushButton_3.setText('Неправильно!')
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setStyleSheet('color: red')
        # Блокаем 2-ю
        # Блокируем кнопку
        self.ui.pushButton_2.setDisabled(True)
        # Меняем текст
        self.ui.pushButton_2.setText('Неправильно')
        # Меняем цвет
        self.ui.pushButton_2.setStyleSheet('color: red')
        # Тоже самое со всеми остальными
        # Блокаем 1-ю
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText('А тут было правильно(')
        self.ui.pushButton.setStyleSheet('color: green')
        # Этот блок готов

    # Кнопка "Молоко"
    def second(self):
        # Блокаем 2-ю
        self.ui.pushButton_2.setStyleSheet('color: red')
        self.ui.pushButton_2.setText('Неправильно!!')
        self.ui.pushButton_2.setDisabled(True)
        # Блокаем 3-ю
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setText('Неправильно')
        self.ui.pushButton_3.setStyleSheet('color: red')
        # Блокаем 1-ю
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText('А тут было правильно!')
        self.ui.pushButton.setStyleSheet('color: green')
        # Этот блок готов

    # Кнопка "Кукурузные палочки"
    def first(self):
        # Блокаем 1-ю
        self.ui.pushButton.setStyleSheet("color: green")
        self.ui.pushButton.setText('Правильно!')
        self.ui.pushButton.setDisabled(True)
        # Блокаем 2-ю
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_2.setText('Не правильно')
        self.ui.pushButton_2.setStyleSheet('color: red')
        # Блокаем 3-ю
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setText('Неправильно')
        self.ui.pushButton_3.setStyleSheet('color: red')
        # Этот блок готов

    # А тут уже потом продолжение будет
    def next(self):
        self.ui.pushButton_4.setText('А тут потом')
        self.ui.pushButton_4.setStyleSheet('color: green')
        # Это потом удали:)
        # Первая кнопка
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton.setStyleSheet("color: black")
        self.ui.pushButton.setText("Кукурузные палочки")
        # Вторая кнопка
        self.ui.pushButton_2.setDisabled(False)
        self.ui.pushButton_2.setStyleSheet("color: black")
        self.ui.pushButton_2.setText("Молоко")
        # Третья кнопка
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_3.setStyleSheet("color: black")
        self.ui.pushButton_3.setText("Хлеб")
        # Сбросим значение кнопки next
        self.ui.pushButton_4.setText("Дальше")
        self.ui.pushButton_4.setStyleSheet("color: black")


# Точка входа
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())