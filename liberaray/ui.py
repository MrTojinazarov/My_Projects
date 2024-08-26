from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel,
    QTableView,
    QHeaderView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem  
from classes import *
from core import *

class MainPage(QWidget):
    def __init__(self)->None:
        super().__init__()
        self.setWindowTitle("Liberary")
        self.showMaximized()
        self.core = Database()


        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()


        self.title_label = QLabel()
        self.title_label.setText("Welcome to Liberary")
        self.title_label.setStyleSheet("color: orange; font-size: 55px;")

        self.login = LineEdit()
        self.login.setPlaceholderText("Enter your login...")

        self.password = LineEdit()
        self.password.setPlaceholderText("Enter your password...")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("color: red; font-size: 25px;")

        self.enter_btn = Button("Enter")
        
        self.registr_btn = Button("Registration")


        # add to widget

        self.v_box.addStretch(100)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.login, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(12)
        self.v_box.addWidget(self.registr_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)

        self.enter_btn.clicked.connect(self.Enter_to_Liberary)
        self.registr_btn.clicked.connect(self.Enter_registr_page)

        
    def Enter_to_Liberary(self):
        # login = self.login.text()
        # password = self.password.text()

        # self.info_label.clear()

        # if not (login and password):
        #     self.info_label.setText("Empty login or password!")
        #     return

        # user = {
        #     'login' : login,
        #     'password' : password
        # }

        # _id = self.core.get_user_id(user)

        # if not _id:
        #     self.info_label.setText("Incorrect login or password")
        #     return
        
        self.close()
        self.open_liberary = LiberaryPage()


    def Enter_registr_page(self):
        self.close()
        self.open_registr_page = RegistrationPage()



class RegistrationPage(QWidget):
    def __init__(self)->None:
        super().__init__()
        self.setWindowTitle("Registration")
        self.showMaximized()
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()


        self.title_label = QLabel()
        self.title_label.setText("Registration")
        self.title_label.setStyleSheet("color: orange; font-size: 55px;")

        self.login = LineEdit()
        self.login.setPlaceholderText("Enter your login...")

        self.password = LineEdit()
        self.password.setPlaceholderText("Enter your password...")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("color: red; font-size: 25px;")

        self.save_btn = Button("Save")
        
        # add to widget

        self.v_box.addStretch(100)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.login, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(100)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.Registr_user)

    def Registr_user(self):
        login = self.login.text()
        password = self.password.text()

        self.info_label.clear()

        if not (login and password):
            self.info_label.setText("Empty login or password")
            return

        user = {
            'login' : login,
            'password' : password
        }

        err = self.core.Insert_User(user)

        if err:
            self.info_label.setText("User already exist")
            return
        
        self.close()
        self.open_liberary = LiberaryPage()
        

class LiberaryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library")
        self.setFixedSize(1200, 700)
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_btn = QVBoxLayout()
        self.h_btn = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Id")
        self.search.setFixedSize(230, 45)
        self.search.setStyleSheet("font-size: 25px; border-radius: 5px; padding-left: 10px;")

        self.update_btn = Button("Update")
        self.update_btn.setFixedSize(150,50)
        self.delete_btn = Button("Delete")
        self.delete_btn.setFixedSize(150,50)
        self.add_btn = Button("Add book")
        self.add_btn.setFixedSize(150,50)
        self.exit = QPushButton("Exit")
        self.exit.setFixedSize(150, 50)
        self.exit.setStyleSheet("""
                                background: Light blue; 
                                color: white; 
                                font-size: 25px;
                                border-radius: 5px;""")

        self.h_btn.addWidget(self.search)
        self.h_btn.addWidget(self.update_btn)
        self.h_btn.addWidget(self.delete_btn)
        self.h_btn.addWidget(self.add_btn)
        self.h_btn.addWidget(self.exit)
        self.v_btn.addLayout(self.h_btn)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Id', 'Name', 'Author', 'Genre', 'Quantity'])

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.v_btn.addWidget(self.table_view)


        self.setLayout(self.v_btn)
        self.table_view.clicked.connect(self.on_cell_clicked)
        self.update_btn.clicked.connect(self.go_to_update)
        self.delete_btn.clicked.connect(self.go_to_delete)
        self.add_btn.clicked.connect(self.add_books)
        self.exit.clicked.connect(self.back)
        self.load_data()

    def back(self):
        self.close()

    def on_cell_clicked(self, index):
        if index.column() == 0:
            data = self.model.itemFromIndex(index).text()
            self.search.setText(data)

    def load_data(self):
        data = self.core.get_all_books()

        self.model.setRowCount(len(data))
        for row, items in  enumerate(data):
            for column, title in enumerate(items):
                self.model.setItem(row, column, QStandardItem(str(title)))

    def go_to_delete(self):

        id_ = self.search.text()
        err = self.core.delete_book(id_)
        self.load_data()

    def add_books(self):
        self.close()
        self.open_add = AddBooksPage()

    def go_to_update(self):
            
        id_ = self.search.text()

        if id_:
            row_data = None
            for row in range(self.model.rowCount()):
                item = self.model.item(row, 0)
                if item and item.text() == id_:
                    row_data = [
                        self.model.item(row, 0).text(),
                        self.model.item(row, 1).text(),
                        self.model.item(row, 2).text(),
                        self.model.item(row, 3).text(),
                        self.model.item(row, 4).text()
                    ]
                    break


            print(row_data)
            self.close()
            self.update_page = UpdatePage(row_data)

class AddBooksPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Add Books")
        self.setFixedSize(500, 700)
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title = QLabel()
        self.title.setText("Add book to data")
        self.title.setStyleSheet("font-size: 50px; color: orange;")

        self.name_btn = LineEdit()
        self.name_btn.setPlaceholderText("Book name")

        self.author_btn = LineEdit()
        self.author_btn.setPlaceholderText("Author name")

        self.genre_btn = LineEdit()
        self.genre_btn.setPlaceholderText("Genre")

        
        self.quantity_btn = LineEdit()
        self.quantity_btn.setPlaceholderText("Quantity")


        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 20px; color: red;")

        self.save_btn = Button("Save")

        self.v_box.addStretch(10)
        self.v_box.addWidget(self.title, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.name_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.author_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.genre_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.quantity_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.add_database)


    def add_database(self):

        name = self.name_btn.text()
        author = self.author_btn.text()
        genre = self.genre_btn.text()
        quantity = self.quantity_btn.text()
        self.info_label.clear()
        if not (name and author and genre and quantity):
            self.info_label.setText("Empty area, please fill all of them")
            return
        
        book = {
                'name' : name,
                'author' : author,
                'genre' : genre,
                'quantity' : quantity
            }

        err = self.core.Add_book(book)
        
        if err:
            self.info_label.setText(err)
            return
        
        self.close()

        self.open_library = LiberaryPage()


class UpdatePage(QWidget):
    def __init__(self, data: list) -> None:
        super().__init__()
        self.setWindowTitle("Update")
        self.setFixedSize(500, 700)
        self.core = Database()
        self.data = data

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title = QLabel()
        self.title.setText("Update book data")
        self.title.setStyleSheet("font-size: 50px; color: orange;")

        self.name_btn = LineEdit()
        self.name_btn.setText(self.data[1])

        self.author_btn = LineEdit()
        self.author_btn.setText(self.data[2])

        self.genre_btn = LineEdit()
        self.genre_btn.setText(self.data[3])
        
        self.quantity_btn = LineEdit()
        self.quantity_btn.setText(self.data[4])

        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-size: 20px; color: red;")

        self.save_btn = Button("Save")

        self.v_box.addStretch(10)
        self.v_box.addWidget(self.title, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.name_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.author_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.genre_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.quantity_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.update_from_database)

    def update_from_database(self):

        name = self.name_btn.text()
        author = self.author_btn.text()
        genre = self.genre_btn.text()
        quantity = self.quantity_btn.text()
        self.info_label.clear()
        if not (name and author and genre and quantity):
            self.info_label.setText("Empty area, please fill all of them")
            return
        
        book = {
                'id' : self.data[0],
                'name' : name,
                'author' : author,
                'genre' : genre,
                'quantity' : quantity
            }

        err = self.core.Update_book(book)
        
        if err:
            self.info_label.setText(err)
            return
        
        self.close()
        self.open_library = LiberaryPage()




app = QApplication([])
liberary = MainPage()
liberary.show()
app.exec_()

