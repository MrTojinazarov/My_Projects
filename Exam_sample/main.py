from PyQt5.QtWidgets import QApplication
from ui import Window
from core import *

def main():
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()