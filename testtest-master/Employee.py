import sys
import sqlite3
import main
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class StaffWin(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        if len(args) > 2:
            self.id = args[2]
        else:
            self.id = -1
        self.m = args[1]
        try:
            uic.loadUi('Staff.ui', self)
        except Exception as ex:
            print(ex)
        # self.textEdit_2.setPlainText(str(self.id))
        self.con = sqlite3.connect("1.db")
        self.pushButton.clicked.connect(self.a1)
        cur = self.con.cursor()
        que = "SELECT Name FROM Job"
        jobs = cur.execute(que, ())
        self.con.commit()
        for i in jobs:
            self.staff.addItem(i[0])

    def a1(self):
        try:
            if self.id == -1:
                cur = self.con.cursor()
                que = "INSERT INTO Employee (Name) VALUES (?)"
                cur.execute(que, (self.staff.toPlainText(), self.Name))
                self.con.commit()
                self.close()
            else:
                cur = self.con.cursor()
                que = "UPDATE Employee SET Name = ? WHERE ID = ?"
                cur.execute(que, (self.textEdit_2.toPlainText(), self.id))
                self.con.commit()
                self.close()

        except Exception as ex:
            print(ex)

    def closeEvent(self, evnt):
        super(StaffWin, self).closeEvent(evnt)
        self.m.updateForm()