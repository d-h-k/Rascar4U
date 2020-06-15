#python
from PyQt5.QtWidgets import *
from PyQt5.uic import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("1_UI.ui",self)

    def clickedRight(self):
        print("Right")
    
    def clickedLeft(self):
        print("Left")

    def clickedGo(self):
        print("Go")

    def clickedBack(self):
        print("Back")

    def clickedMid(self):
        print("Mid")

app = QApplication([])
win = MyApp()
win.show()
app.exec()