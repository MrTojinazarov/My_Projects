from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit
)

class Button(QPushButton):
    def __init__(self, text = ""):
        super().__init__(text)

        self.setFixedSize(300, 50)
        self.setStyleSheet("""
                           background: orange;
                           color: white;
                           border-radius: 5px;
                           font-size: 25px
                           """)

class LineEdit(QLineEdit):
    def __init__(self, text = ""):
        super().__init__(text)

        self.setFixedSize(300, 50)
        self.setStyleSheet("""
                           border-radius: 5px;
                           padding: 5px;
                           padding-left: 10px;
                           font-size: 25px;
                           """)