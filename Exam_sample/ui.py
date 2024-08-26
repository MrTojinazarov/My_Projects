from PyQt5.QtWidgets import(
    QWidget,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import Qt

from core import *

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Product_list")
        self.setFixedSize(800, 500)
        self.setStyleSheet("""
                QLineEdit{
                            font-size: 20px;
                            border-radius: 8px;  
                            padding: 5px;
                            padding-left: 10px;
                           }
                           
                QLabel{
                            font-size: 35px;
                            color: orange;
                        }
                
                QPushButton{
                            font-size: 25px;
                            color: white;
                            background: orange;
                            border-radius: 8px;
                           }""")
        self.initUi()

    def initUi(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.title_name = QLabel()
        self.title_name.setText("Product List")
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.enter = QPushButton("Enter")
        self.enter.setFixedSize(200, 50)
        self.enter.clicked.connect(self.Enter_to_Product)
        self.registr = QPushButton("Registration")
        self.registr.setFixedSize(200, 50)
        self.registr.clicked.connect(self.Go_Registr)

        self.v_box.addStretch(100)
        self.v_box.addWidget(self.title_name, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.username, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.enter, 0, Qt.AlignCenter)
        self.v_box.addStretch(20)
        self.v_box.addWidget(self.registr, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)
        
    def Go_Registr(self):
        self.open_registr_page = RegistrationPage()
        self.close()

    def Enter_to_Product(self):
        login = self.username.text()
        password = self.password.text()

        if not (login and password):
            return

        user = {
            'login' : login,
            'password' : password
        }

        id = self.core.get_user_data(user)
        if not id:
            return
        
        self.enter_product_page = ProductPage()
        self.close()


class RegistrationPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Product_list")
        self.setFixedSize(800, 500)
        self.setStyleSheet("""
                QLineEdit{
                            font-size: 20px;
                            border-radius: 8px;  
                            padding: 5px;
                            padding-left: 10px;
                           }
                           
                QLabel{
                            font-size: 35px;
                            color: orange;
                        }
                
                QPushButton{
                            font-size: 25px;
                            color: white;
                            background: orange;
                            border-radius: 8px;
                           }""")
        self.initUi()

    def initUi(self):
        self.v_box = QVBoxLayout()


        self.title_name = QLabel()
        self.title_name.setText("Registration")
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.save_btn = QPushButton("Save User")
        self.save_btn.setFixedSize(200, 50)
        self.save_btn.clicked.connect(self.save_to_database)

        self.v_box.addStretch(100)
        self.v_box.addWidget(self.title_name, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.username, 0, Qt.AlignCenter)
        self.v_box.addStretch(10)
        self.v_box.addWidget(self.password, 0, Qt.AlignCenter)
        self.v_box.addStretch(20)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignCenter)
        self.v_box.addStretch(80)

        self.setLayout(self.v_box)

        self.show()

    def save_to_database(self):
        
        username = self.username.text()
        password = self.password.text()

        user = {
            'login' : username,
            'password' : password
        }

        err = self.core.Insert_User(user)


class ProductPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Products")
        self.setFixedSize(800, 500)
        self.show()

        self.initUI()

    def initUI(self):

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        

        self.delete_btn = QPushButton("Delete")
        self.update_btn = QPushButton("Update")
