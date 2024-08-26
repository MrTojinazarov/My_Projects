from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QTableView,
    QHeaderView,
    QApplication,
    QMessageBox
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from core import *
from classes import *

class MainPage(QWidget):
    def __init__(self)->None:
        super().__init__()
        self.setWindowTitle("Main")
        self.setFixedSize(1200, 700)
        self.core = Database()

        self.initUI()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = QLabel()
        self.title_label.setText("Welcome to our Market")
        self.title_label.setStyleSheet("font-size: 55px; color: orange;")

        self.login = LineEdit()
        self.login.setPlaceholderText("Login...")

        self.password = LineEdit()
        self.password.setPlaceholderText("Password...")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 25px; color: red;")

        self.enter_btn = Button("Enter")
        self.registr_btn = Button("Registration")

        self.v_box.addStretch(40)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.login, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.registr_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(30)

        self.setLayout(self.v_box)

        self.enter_btn.clicked.connect(self.enter_market)
        self.registr_btn.clicked.connect(self.registration)

    def enter_market(self):
        # login = self.login.text()
        # password = self.password.text()

        # self.info_label.clear()

        # if not (password and login):
        #     self.info_label.setText("Empty login or password")
        #     return
        
        # user = {
        #     'login' : login,
        #     'password' : password
        # }

        # id_ = self.core.get_user_id(user)

        # if not id_:
        #     self.info_label.setText("Incorrect login or password")
        #     return
        
        self.close()
        self.open_market = Market()

    def registration(self):
        self.open_registr = RegistrationPage()

class RegistrationPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Registration")
        self.setFixedSize(1200, 700)
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = QLabel()
        self.title_label.setText("Registration")
        self.title_label.setStyleSheet("font-size: 55px; color: orange;")

        self.login = LineEdit()
        self.login.setPlaceholderText("Login...")

        self.password = LineEdit()
        self.password.setPlaceholderText("Password...")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 25px; color: red;")

        self.save_btn = Button("Save")


        self.v_box.addStretch(40)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.login, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(30)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.save_user)

    def save_user(self):
        login = self.login.text()
        password = self.password.text()

        self.info_label.clear()

        if not (password and login):
            self.info_label.setText("Empty login or password")
            return
        
        if len(login) < 8 and len(password) < 8:
            self.info_label.setText("Login va Password 8 ta belgidan kam bo'lmasin")

        user = {
            'login' : login,
            'password' : password
        }

        err = self.core.add_user_data(user)

        if err:
            self.info_label.setText(err)
            return
        self.close()

class Market(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Market")
        self.setFixedSize(1200, 800)
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.search = LineEdit()
        self.search.setPlaceholderText("Id")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 25px; color: red;")

        self.update_btn = Button("Update")
        self.update_btn.setFixedSize(150, 50)
        self.delete_btn = Button("Delete")
        self.delete_btn.setFixedSize(150, 50)
        self.add_item_btn = Button("Add item")
        self.add_item_btn.setFixedSize(150, 50)
        self.exit_btn = Button("Exit")
        self.exit_btn.setFixedSize(150, 50)

        self.h_box.addWidget(self.search)
        self.h_box.addWidget(self.update_btn)
        self.h_box.addWidget(self.delete_btn)
        self.h_box.addWidget(self.add_item_btn)
        self.h_box.addWidget(self.exit_btn)

        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.info_label)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Id", "Items", "Price", "Quantity"])

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.v_box.addWidget(self.table_view)

        self.setLayout(self.v_box)

        self.load_data(self.core.get_all_items())
        self.table_view.clicked.connect(self.on_cell_clicked)
        self.update_btn.clicked.connect(self.update_item)
        self.delete_btn.clicked.connect(self.delete_item)

    def on_cell_clicked(self, index):
        if index.column() == 0:
            data = self.model.itemFromIndex(index).text()
            self.search.setText(data)

    def load_data(self, data: list):
        
        for row, items in enumerate(data):
            for column, title in enumerate(items):
                self.model.setItem(row, column, QStandardItem(str(title)))

    def update_item(self):
        id = self.search.text()

        if not id.isdigit():
            self.info_label.setText("Faqat id kiritilsin")
            return

        if id:
            row_data = None
            for row in range(self.model.rowCount()):
                item = self.model.item(row, 0)
                if item and item.text() == id:
                    row_data = [
                        self.model.item(row, 0).text(),
                        self.model.item(row, 1).text(),
                        self.model.item(row, 2).text(),
                        self.model.item(row, 3).text()
                    ]
                    break

            self.open_market = UpdatePage(row_data)
            self.close()

    def delete_item(self):

        item_id = self.search.text()

        if not (item_id and item_id.isdigit()):
            self.info_label.setText("Incorrect id, Enter only id number")
            return
        
        if item_id:

            self.delete = self.core.delete_item(item_id)

        self.load_data()


class UpdatePage(QWidget):
    def __init__(self, data: list) -> None:
        super().__init__()
        self.setWindowTitle("Update")
        self.setFixedSize(500, 800)
        self.core = Database()
        self.data = data
        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = QLabel()
        self.title_label.setText("Update Item")
        self.title_label.setStyleSheet("font-size: 55px; color: orange;")

        self.item = LineEdit()
        self.item.setText(self.data[1])

        self.price = LineEdit()
        self.price.setText(self.data[2])

        self.quantity = LineEdit()
        self.quantity.setText(self.data[3])

        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 25px; color: red;")

        self.save_btn = Button("Save")


        self.v_box.addStretch(40)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.item, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.price, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.quantity, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(30)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.update_from_data)

    def update_from_data(self):

        item = self.item.text()
        price = self.price.text()
        quantity = self.quantity.text()

        if not (item and price and quantity):
            self.info_label.setText("Fill all area, please")
            return
        
        data = {
            'id' : self.data[0],
            'item' : item,
            'price' : price,
            'quantity' : quantity
        }

        err = self.core.Update_item(data)

        if not err:
            self.info_label.setText(err)

        self.close()
        self.open_market = Market()



app = QApplication([])
market = MainPage()
market.show()
app.exec_()