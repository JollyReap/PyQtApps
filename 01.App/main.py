import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from devs import *



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

   
    def third(self):
        
        self.ui.pushButton_3.setText('Неправильно!')
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setStyleSheet('color: red')
        
        
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_2.setText('Неправильно')
        self.ui.pushButton_2.setStyleSheet('color: red')

        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText('А тут было правильно(')
        self.ui.pushButton.setStyleSheet('color: green')
        

  
    def second(self):

        self.ui.pushButton_2.setStyleSheet('color: red')
        self.ui.pushButton_2.setText('Неправильно!!')
        self.ui.pushButton_2.setDisabled(True)
        
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setText('Неправильно')
        self.ui.pushButton_3.setStyleSheet('color: red')
        
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText('А тут было правильно!')
        self.ui.pushButton.setStyleSheet('color: green')
     

    
    def first(self):
      
        self.ui.pushButton.setStyleSheet("color: green")
        self.ui.pushButton.setText('Правильно!')
        self.ui.pushButton.setDisabled(True)
        
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_2.setText('Не правильно')
        self.ui.pushButton_2.setStyleSheet('color: red')
       
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_3.setText('Неправильно')
        self.ui.pushButton_3.setStyleSheet('color: red')
        

    
    def next(self):
        self.ui.pushButton_4.setText('А тут потом')
        self.ui.pushButton_4.setStyleSheet('color: green')
      
        
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton.setStyleSheet("color: black")
        self.ui.pushButton.setText("Кукурузные палочки")
       
        self.ui.pushButton_2.setDisabled(False)
        self.ui.pushButton_2.setStyleSheet("color: black")
        self.ui.pushButton_2.setText("Молоко")
       
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_3.setStyleSheet("color: black")
        self.ui.pushButton_3.setText("Хлеб")
     
        self.ui.pushButton_4.setText("Дальше")
        self.ui.pushButton_4.setStyleSheet("color: black")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
