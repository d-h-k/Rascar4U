from PyQt5.QtWidgets import *
from PyQt5.uic import * 
from PyQt5 import QtSql

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("hi.ui", self)
        
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("3.34.198.179")        
        self.db.setDatabaseName("dev16")
        self.db.setUserName("dev16")
        self.db.setPassword("1234")
        ok = self.db.open()
        print(ok)        
        
self.query = QtSql.QSqlQuery("select * from command");
        
        while (self.query.next()):
            self.record = self.query.record()
            str = "%s | %6s | %5s | %d" % (self.record.value(0).toString(), self.record.value(1), self.record.value(2), self.record.value(3))
            print(str)
    

app = QApplication([])
win = MyApp()
win.show()
app.exec()
