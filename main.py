from PyQt5.QtWidgets import QApplication
from ui import *

def main():
    app = QApplication([])
    blog = MainPage()
    blog.show()
    app.exec_()

if __name__ == "__main__":
    main()