from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableView,
    QHeaderView,
    QPushButton
)
from time import ctime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from classes import *
from core import *

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Blog Post")
        self.setFixedSize(1200, 700)

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = Label()
        self.title_label.setText("Bosh sahifa")

        self.enter_system = Button("Tizimga kirish")
        self.registr = Button("Ro'yxatdan o'tish")

        self.v_box.addStretch(80)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.enter_system, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.registr, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)

        self.registr.clicked.connect(self.Enter_registr_page)
        self.enter_system.clicked.connect(self.Open_blog_page)

    def Enter_registr_page(self):
        self.close()
        self.open_registr = RegistrationPage()

    def Open_blog_page(self):
        self.close()
        self.checking_login = EnterSystemPage()

class EnterSystemPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tizimga Kirish")
        self.setFixedSize(1200, 800)
        self.core = Database()

        self.initUI()
        self.show()  

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = Label()
        self.title_label.setText("Tizimga kirish")

        self.usename = LineEdit()
        self.usename.setPlaceholderText("Username")
        
        self.password = LineEdit()
        self.password.setPlaceholderText("Password")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("color: red; font-size: 20px;")

        self.enter_btn = Button("Enter")
        self.back_btn = QPushButton("Exit")
        self.back_btn.setFixedSize(250, 50)
        self.back_btn = Back_Button("Back")


        self.v_box.addStretch(80)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.usename, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.enter_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.back_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)


        self.setLayout(self.v_box)

        self.enter_btn.clicked.connect(self.Checking_login)
        self.back_btn.clicked.connect(self.Back_to_main_page)

    def Checking_login(self):

        username = self.usename.text()
        password = self.password.text()

        if not (username and password):
            self.info_label.setText("Empty area, please fill all of them!")
            return
        
        user = {
            'login' : username,
            'password' : password
        }

        user_id = self.core.Get_user_id(user)

        if user_id:
            self.close()
            self.open_blog_post = BlogPostPage(username)
        else:
            self.info_label.setText("Incorrect login or password")
            return

    def Back_to_main_page(self):
        self.close()
        self.open_main = MainPage()

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration")
        self.setFixedSize(1200, 800)
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = Label()
        self.title_label.setText("Ro'yxatdan o'tish")

        self.name_surname = LineEdit()
        self.name_surname.setPlaceholderText("Ism, familia")

        self.phonenumber = LineEdit()
        self.phonenumber.setInputMask("+999999999999")

        self.usename = LineEdit()
        self.usename.setPlaceholderText("Username")
        
        self.password = LineEdit()
        self.password.setPlaceholderText("Password")

        self.info_label = QLabel()
        self.info_label.setStyleSheet("color: red; font-size: 20px;")

        self.save_btn = Button("Save")
        self.back_btn = Back_Button("Back")


        self.v_box.addStretch(80)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.name_surname, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.phonenumber, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.usename, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.back_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)

        self.back_btn.clicked.connect(self.Back_to_main_page)
        self.save_btn.clicked.connect(self.Registr_to_database)

    def Registr_to_database(self):

        name_surname = self.name_surname.text()
        phone_num = self.phonenumber.text()
        username = self.usename.text()
        passsword = self.password.text()

        self.info_label.clear()

        if not (name_surname and phone_num and username and passsword):
            self.info_label.setText("Empty area, Please fill all of them")
            return
        
        if len(username) < 8 and len(passsword) < 8:
            self.info_label.setText("Username va password 8 ta belgidan kam bo'lmasin!")
            return
        
        user = {
            'person' : name_surname,
            'phone' : phone_num,
            'login' : username,
            'password' : passsword
        }

        err = self.core.Insert_user(user)

        if err:
            self.info_label.setText(err)
            return
        
        self.close()
        self.open_blog_page = BlogPostPage(username)

    
    def Back_to_main_page(self):
        self.close()
        self.open_main = MainPage()


class BlogPostPage(QWidget):
    def __init__(self, login: str):
        super().__init__()
        self.setWindowTitle("Blog Post")
        self.setFixedSize(1200, 700)
        self.login = login
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.write_post = Button("Post yozish")
        self.my_posts = Button("Postlarim")
        self.exit_btn = QPushButton("Exit")
        self.exit_btn.setFixedSize(250, 50)
        self.exit_btn = Back_Button("Back")


        self.h_box.addWidget(self.write_post)
        self.h_box.addWidget(self.my_posts)
        self.h_box.addWidget(self.exit_btn)

        self.v_box.addLayout(self.h_box)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Username', 'Posts', 'Time'])

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.v_box.addWidget(self.table_view)

        self.setLayout(self.v_box)

        self.write_post.clicked.connect(self.OpenWritePage)
        self.my_posts.clicked.connect(self.OpenMyPostsPage)
        self.exit_btn.clicked.connect(self.Exit_from_programm)

        self.Load_all_posts()


    def Load_all_posts(self):

        all_posts = self.core.Get_all_posts()

        for row, items in enumerate(all_posts):
            for i in range (1, len(items)):
                self.model.setItem(row, i-1, QStandardItem(str(items[i]))) 


    def OpenWritePage(self):
        self.close()
        self.open_write_page = WritePostPage(self.login)

    def OpenMyPostsPage(self):
        self.close()
        self.open_my_posts = MyPostsPage(self.login)

    def Exit_from_programm(self):
        self.close()

class WritePostPage(QWidget):
    def __init__(self, login: str):
        super().__init__()
        self.setWindowTitle("Write a post")
        self.setFixedSize(1200, 700)
        self.login = login
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.title_label = Label()
        self.title_label.setText("Post yozish")

        self.write_post = LineEdit()
        self.write_post.setPlaceholderText("Post yozing")
        self.write_post.setFixedSize(500, 60)

        self.info_label = QLabel()
        self.info_label.setStyleSheet("color: red; font-size: 20px;")

        self.set_post = Button("Yuklash")
        self.back_btn = Back_Button("Back")


        self.v_box.addStretch(100)
        self.v_box.addWidget(self.title_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(15)
        self.v_box.addWidget(self.write_post, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.set_post, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.back_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)

        self.set_post.clicked.connect(self.Upload_to_database)
        self.back_btn.clicked.connect(self.Back_from_page)

    def Upload_to_database(self):

        blog_post = self.write_post.text()
        time = ctime()

        if not blog_post:
            self.info_label.setText("Write a blog")
            return

        blog = {
            'login' : self.login,
            'post' : blog_post,
            'datetime' : time
        }

        err = self.core.UploadPost(blog)

        if err:
            self.info_label.setText(err)
            return
        self.close()
        self.open_blog_page = BlogPostPage(self.login)
    
    def Back_from_page(self):
        self.close()
        self.open_main = BlogPostPage(self.login)

class MyPostsPage(QWidget):
    def __init__(self, login: str):
        super().__init__()
        self.setWindowTitle("My posts")
        self.setFixedSize(1200, 800)
        self.login = login
        self.core = Database()

        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Username', 'Posts', 'Time'])

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.v_box.addWidget(self.table_view)

        self.back_btn = Back_Button("Back")

        self.v_box.addWidget(self.back_btn, 0, Qt.AlignCenter)

        self.setLayout(self.v_box)
        self.load_table()
        self.back_btn.clicked.connect(self.Back_to_Page)

    def load_table(self):

        my_posts = self.core.Get_own_data(self.login)

        for row, items in enumerate(my_posts):
            for i in range (1, len(items)):
                self.model.setItem(row, i-1, QStandardItem(str(items[i])))

    def Back_to_Page(self):
        self.close()
        self.back_to_blog = BlogPostPage(self.login)
