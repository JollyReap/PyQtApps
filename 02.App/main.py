import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.accept)

    def accept(self):
        if self.ui.radioButton.isChecked():
            self.ui.pushButton.setText('Неправильно!')
            self.ui.pushButton.setStyleSheet('background-color: red')
        if self.ui.radioButton_2.isChecked():
            self.ui.pushButton.setText('Правильно!')
            self.ui.pushButton.setStyleSheet('background-color: green')
        if self.ui.radioButton_3.isChecked():
            self.ui.pushButton.setText('Неправильно!')
            self.ui.pushButton.setStyleSheet('background-color: red')
        if self.ui.radioButton_4.isChecked():
            self.ui.pushButton.setText('Неправильно')
            self.ui.pushButton.setStyleSheet('background-color: red')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())