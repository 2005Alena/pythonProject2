import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QTableView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import second, RegForm, sqlite3, Employee, Hotel


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = HotelWidget()
        self.tab2 = EmployeeWidget()
        self.tab3 = RegionWidget()
        self.tab4 = JobWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Отели")
        self.tabs.addTab(self.tab2, "Работники")
        self.tabs.addTab(self.tab3, "Регионы")
        self.tabs.addTab(self.tab4, "Должности")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class HotelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('1.db')
        # И откроем подключение
        db.open()

        self.view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, db)
        self.model.setTable('Hotel')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)
        self.pushButton1 = QPushButton("Добавить")
        self.layout.addWidget(self.pushButton1)
        self.pushButton2 = QPushButton("Изменить")
        self.layout.addWidget(self.pushButton2)
        self.pushButton3 = QPushButton("Удалить")
        self.layout.addWidget(self.pushButton3)
        self.pushButton1.clicked.connect(self.open_hot_form)
        self.pushButton2.clicked.connect(self.change)
        self.pushButton3.clicked.connect(self.ddel)

    def open_hot_form(self):
        self.form1 = Hotel.HotWin(self, self)
        self.form1.show()

    def change(self):
        self.form2 = Hotel.HotWin(self, self, self.view.selectionModel().selectedIndexes()[0].data())
        self.form2.show()

    def updateForm(self):
        self.model.select()

    def ddel(self):
        self.con = sqlite3.connect("1.db")
        cur = self.con.cursor()
        que = "DELETE FROM Hotel WHERE Name = ?"
        cur.execute(que, (self.view.selectionModel().selectedIndexes()[0].data(),))
        self.con.commit()
        self.updateForm()


class EmployeeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('1.db')
        # И откроем подключение
        db.open()

        self.view = QTableView(self)
       # self.view.setSelectionBehavior(QTableView.SelectRows)
       # self.view.setSelectionMode(QTableView.SingleSelection)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, db)
        self.model.setTable('Employee')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)
        self.pushButton1 = QPushButton("Добавить")
        self.layout.addWidget(self.pushButton1)
        self.pushButton2 = QPushButton("Изменить")
        self.layout.addWidget(self.pushButton2)
        self.pushButton3 = QPushButton("Удалить")
        self.layout.addWidget(self.pushButton3)
        self.pushButton1.clicked.connect(self.open_emp_form)
        self.pushButton2.clicked.connect(self.change)
        self.pushButton3.clicked.connect(self.ddel)

    def open_emp_form(self):
        self.form1 = Employee.StaffWin(self, self)
        self.form1.show()

    def change(self):
        try:
            self.form2 = Employee.StaffWin(self, self, self.view.selectionModel().selectedIndexes()[0].data())
            self.form2.show()
        except Exception as ex:
            print(ex)

    def updateForm(self):
        self.model.select()

    def ddel(self):
        self.con = sqlite3.connect("1.db")
        cur = self.con.cursor()
        que = "DELETE FROM Employee WHERE ID = ?"
        cur.execute(que, (self.view.selectionModel().selectedIndexes()[0].data(),))
        self.con.commit()
        self.updateForm()

class RegionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('1.db')
        # И откроем подключение
        db.open()

        self.view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, db)
        self.model.setTable('Region')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)
        self.pushButton1 = QPushButton("Добавить")
        self.layout.addWidget(self.pushButton1)
        self.pushButton2 = QPushButton("Изменить")
        self.layout.addWidget(self.pushButton2)
        self.pushButton3 = QPushButton("Удалить")
        self.layout.addWidget(self.pushButton3)
        self.pushButton1.clicked.connect(self.open_reg_form)
        self.pushButton2.clicked.connect(self.change)
        self.pushButton3.clicked.connect(self.ddel)

    def open_reg_form(self):
        self.form1 = RegForm.RegFormWin(self, self)
        self.form1.show()

    def change(self):
        self.form2 = RegForm.RegFormWin(self, self, self.view.selectionModel().selectedIndexes()[0].data())
        self.form2.show()

    def updateForm(self):
        self.model.select()

    def ddel(self):
        self.con = sqlite3.connect("1.db")
        cur = self.con.cursor()
        que = "DELETE FROM Region WHERE Name = ?"
        cur.execute(que, (self.view.selectionModel().selectedIndexes()[0].data(), ))
        self.con.commit()
        self.updateForm()


class JobWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('1.db')
        # И откроем подключение
        db.open()

        self.view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, db)
        self.model.setTable('Job')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)
        self.pushButton1 = QPushButton("Добавить")
        self.layout.addWidget(self.pushButton1)
        self.pushButton2 = QPushButton("Изменить")
        self.layout.addWidget(self.pushButton2)
        self.pushButton3 = QPushButton("Удалить")
        self.layout.addWidget(self.pushButton3)
        self.pushButton1.clicked.connect(self.open_second_form)
        self.pushButton2.clicked.connect(self.change)
        self.pushButton3.clicked.connect(self.ddel)

    def open_second_form(self):
        self.form1 = second.SecondWindow(self, self)
        self.form1.show()

    def change(self):
        self.form2 = second.SecondWindow(self, self, self.view.selectionModel().selectedIndexes()[0].data())
        self.form2.show()

    def updateForm(self):
        self.model.select()

    def ddel(self):
        self.con = sqlite3.connect("1.db")
        cur = self.con.cursor()
        que = "DELETE FROM Job WHERE Name = ?"
        cur.execute(que, (self.view.selectionModel().selectedIndexes()[0].data(), ))
        self.con.commit()
        self.updateForm()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
