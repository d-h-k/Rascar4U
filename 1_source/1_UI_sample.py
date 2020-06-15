#python
from PyQt5.QtWidgets import *
from PyQt5.uic import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("1_UI.ui",self)


app = QApplication([])
win = MyApp()
win.show()
app.exec()