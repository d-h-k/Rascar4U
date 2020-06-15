from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5 import QtSql

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("1_UI.ui", self)
        
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("3.34.124.67")        
        self.db.setDatabaseName("dev15")
        self.db.setUserName("dev15")
        self.db.setPassword("1234")
        ok = self.db.open()
        print(ok)        
        
        self.query = QtSql.QSqlQuery("select * from command");

        while (self.query.next()):
            self.record = self.query.record()
            str = "%s | %10s | %10s | %4d" % (self.record.value(0).toString(), self.record.value(1), self.record.value(2), self.record.value(3))
            self.text.appendPlainText(str)
        
    def clickedRight(self):
        self.query.prepare("insert into command (time, cmd_string, arg_string, is_finish) values (:time, :cmd, :arg, :finish)");
        time = QDateTime().currentDateTime()
        self.query.bindValue(":time", time)
        self.query.bindValue(":cmd", "right")
        self.query.bindValue(":arg", "1 sec")
        self.query.bindValue(":finish", 0)
        self.query.exec()
    
    def clickedLeft(self):
        print("left")
    
    def clickedGo(self):
        print("go")
    
    def clickedBack(self):
        print("back")
        
    def clickedMid(self):
        print("mid")
        
app = QApplication([])
win = MyApp()
win.show()
app.exec()

