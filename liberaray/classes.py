from PyQt5.QtWidgets import QPushButton, QLineEdit

class Button(QPushButton):
    def __init__(self, text = ""):
        super().__init__(text)

        self.setFixedSize(350, 50)

        self.setStyleSheet("""
                        background: Orange;
                        color: White;
                        font-size: 25px;
                        border-radius: 5px;
                        """)


class LineEdit(QLineEdit):
    def __init__(self, text=""):
        super().__init__(text)

        self.setFixedSize(350, 50)

        self.setStyleSheet("""
                        background: #98FF98;
                        font-size: 20px;
                        border-radius: 5px;
                        padding: 4px;
                        padding-left: 10px
                        """)