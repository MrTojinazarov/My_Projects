from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

class Button(QPushButton):
    def __init__(self, text = ""):
        super().__init__(text)
        self.setFixedSize(250, 50)

        self.setStyleSheet("""
                           background: orange;
                           color: white;
                           font-size: 25px;
                           border-radius: 5px;
                           """)
        
class LineEdit(QLineEdit):
    def __init__(self, text = ""):
        super().__init__(text)
        self.setFixedSize(250, 50)
        self.setStyleSheet("""
                           font-size: 20px;
                           border-radius: 5px;
                           padding: 5px;
                           padding-left: 10px
                           """)
        
class Label(QLabel):
    def __init__(self, text = ""):
        super().__init__(text)

        self.setStyleSheet("font-size: 55px; color: orange;")  


class Back_Button(QPushButton):
    def __init__(self, text = ""):
        super().__init__(text)

        self.setFixedSize(250, 50)
        self.setStyleSheet("""
                            background: Light blue;
                            font-size: 25px;
                            border-radius: 5px;
                            color: white;
                            """)