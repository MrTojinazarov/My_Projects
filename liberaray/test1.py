from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableView,
    QHeaderView
)

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class ShowUsersPage(QWidget):
    def __init__(self, users_list: list):
        super().__init__()
        self.users_data = users_list
        self.setWindowTitle("Show users")
        self.setGeometry(300, 100, 800, 600)
        self.setStyleSheet("""
            font-size: 20px
        """)

        self.initUI()

    def initUI(self):

        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Id")
        self.line_edit.setFixedWidth(130)
        self.hbox.addWidget(self.line_edit)

        self.update_button = QPushButton("Updete User", self)
        self.update_button.setFixedWidth(130)
        self.update_button.clicked.connect(self.Update_checked_user)
        self.delete_button = QPushButton("Delete User", self)
        self.delete_button.setFixedWidth(130)  
        self.delete_button.clicked.connect(self.Delete_User_data)
        self.exit = QPushButton("Exit", self)
        self.exit.setFixedWidth(130)
        self.exit.clicked.connect(self.back_to_admin_page) 

        self.users_infos = QTableView(self)
        
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Id", "Name", "Username", "Password"])
        self.add_data_to_model(self.users_data)

        self.users_infos.setModel(self.model)

        self.users_infos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hbox2.addWidget(self.users_infos)

        self.hbox.addStretch()
        self.hbox.addWidget(self.update_button)
        self.hbox.addWidget(self.delete_button)
        self.hbox.addWidget(self.exit)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        self.users_infos.clicked.connect(self.on_cell_clicked)
        

        self.show()

    def on_cell_clicked(self, index):
        if index.column() == 0: 
            data = self.model.itemFromIndex(index).text()
            self.line_edit.setText(data)

    def add_data_to_model(self, data):
        if self.model.rowCount() == 0:
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)
        else:
            self.model.removeRows(0, self.model.rowCount())
            self.line_edit.clear()
            for row in data:
                items = [QStandardItem(str(field)) for field in row]
                self.model.appendRow(items)

    def Update_checked_user(self):
        _id = self.line_edit.text()
        if _id:
            row_data = None

            for row in range(self.model.rowCount()):
                item = self.model.item(row, 0)
                if item and item.text() == _id:
                    row_data = [
                        self.model.item(row, 0).text(),
                        self.model.item(row, 1).text(),
                        self.model.item(row, 2).text(),
                        self.model.item(row, 3).text()
                    ]
                    break
            print(row_data)
                
            # self.update_page = UpdatePage(row_data)
            self.update_page.show()
            self.update_page.save_btn.clicked.connect(self.back_show_page)

    def back_show_page(self):
        self.close()
        if self.update_page:
            self.update_page.close()

    def Delete_User_data(self):
        # self.core = Database()
        
        _id = self.line_edit.text()
        user = {
            'id' : _id
        }
        err = self.core.delete_user_data(user)
        if err:
            self.info_label.setText(err)
        
        users_data = self.core.Get_all_users_data()
        users_list = [list(user) for user in users_data]
        self.add_data_to_model(users_list)

    def back_to_admin_page(self):
        self.close()
        # self.back = LoginPage()