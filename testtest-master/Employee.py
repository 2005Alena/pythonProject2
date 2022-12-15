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
        self.con = sqlite3.connect("1.db")
        cur = self.con.cursor()
        if self.id != -1:
            a = 'SELECT * FROM Employee WHERE ID = ?'
            employee = cur.execute(a, (self.id,))
            self.name.setPlainText(employee[1])
            self.surname.setPlainText(employee[2])
            self.patronymic.setPlainText(employee[3])
            self.phone.setPlainText(employee[4])
            self.mail.setPlainText(employee[5])
            self.staff.setCurrentIndex(employee[6])

        self.pushButton.clicked.connect(self.a1)
        que = "SELECT Name, id FROM Job "
        jobs = cur.execute(que, ())
        self.con.commit()
        for i in jobs:
            self.staff.addItem(i[0], userData=i[1])

    def a1(self):
        try:
            if self.id == -1:
                cur = self.con.cursor()
                que = "INSERT INTO Employee (Name, Surname, MiddleName, Phone, [E-mail], IDJob) VALUES (?, ?, ?, ?, ?, ?)"
                cur.execute(que, (self.name.toPlainText(), self.surname.toPlainText(), self.patronymic.toPlainText(), self.phone.toPlainText(), self.mail.toPlainText(), self.staff.itemData(self.staff.currentIndex())))
                print(self.name.toPlainText(), self.surname.toPlainText(), self.patronymic.toPlainText(), self.phone.toPlainText(), self.mail.toPlainText(), self.staff.currentText(), self.staff.itemData(self.staff.currentIndex()))
                self.con.commit()
                self.close()
            else:
                cur = self.con.cursor()
                que = "UPDATE Employee SET Name = ?, Surname = ?, MiddleName = ?, Phone = ?, [E-mail] = ?, IDJob = ? WHERE ID = ?"
                cur.execute(que, (self.name.toPlainText(), self.surname.toPlainText(), self.patronymic.toPlainText(),
                                  self.phone.toPlainText(), self.mail.toPlainText(),
                                  self.staff.itemData(self.staff.currentIndex()), self.id))
                self.con.commit()
                self.close()

        except Exception as ex:
            print(ex)

    def closeEvent(self, evnt):
        super(StaffWin, self).closeEvent(evnt)
        self.m.updateForm()