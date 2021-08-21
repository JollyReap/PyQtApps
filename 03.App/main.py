import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from app import *
from bs4 import BeautifulSoup
import requests


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.parse)
        self.link = "https://browser-info.ru"
        self.response = requests.get(self.link).text
        self.soup = BeautifulSoup(self.response, 'lxml')
        self.ui.pushButton_2.clicked.connect(self.delete)

    def parse(self):
        block = self.soup.find('div', id='tool_padding')
 
        check_js = block.find('div', id='javascript_check')
        status_js = check_js.find_all('span')[1].text
       
        check_ck = block.find('div', id='cookie_check')
        status_ck = check_ck.find_all('span')[1].text
   
        check_fh = block.find('div', id='flash_version')
        status_fh = check_fh.find_all('span')[1].text
        self.ui.label.setText(f'JavaScript:{status_js}\nCookie:{status_ck}\nFlash:{status_fh}')

    def delete(self):
        self.ui.label.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
