'''
from PyQt5 import QtSql

self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
self.db.setHostName("")#server's ip
self.db.setDatabaseName("dev16")#your name
self.db.setUserName("dev16")#your name
self.db.setPassword("1234")#your passwd
ok = self.db.open()
print(ok)
'''

