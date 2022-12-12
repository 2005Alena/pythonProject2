import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QTableView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import second


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
        self.tab1 = StaffWidget()
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


class StaffWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('1.db')
        # И откроем подключение
        db.open()

        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('Hotel')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Add")
        self.layout.addWidget(view)
        self.layout.addWidget(self.pushButton1)
        self.setLayout(self.layout)


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

        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('Employee')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Add")
        self.layout.addWidget(view)
        self.layout.addWidget(self.pushButton1)
        self.setLayout(self.layout)

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

        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('Region')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)
        self.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Add")
        self.layout.addWidget(view)
        self.layout.addWidget(self.pushButton1)
        self.setLayout(self.layout)

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
        self.pushButton2.clicked.connect(self.z1)

    def open_second_form(self):
        self.form1 = second.SecondWindow(self, self)
        self.form1.show()

    def z1(self):
        self.form2 = second.SecondWindow(self, self,self.view.selectionModel().selectedIndexes()[0].data())
        self.form2.show()

    def w1(self):
        self.model.select()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
