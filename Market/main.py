from PyQt5.QtWidgets import QApplication
from ui import *

def main():
    app = QApplication([])
    market = MainPage()
    market.show()
    app.exec_()

if __name__ == "__main__":
    main()