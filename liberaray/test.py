import sys
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from core import *

class TableViewExample(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Database()

        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['ID', 'Nomi', 'Narxi'])

        self.populate_model(self.core.get_all_books())

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        self.setLayout(layout)

        self.setWindowTitle("QTableView va QStandardItemModel misoli")
        self.resize(600, 400)

    def populate_model(self, data):

        self.model.setRowCount(len(data))
        for row, item_data in enumerate(data):
            for column, value in enumerate(item_data):
                self.model.setItem(row, column, QStandardItem(str(value)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableViewExample()
    window.show()
    sys.exit(app.exec_())



# class LiberaryPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Liberary")
#         self.setFixedSize(1100, 600)
#         self.core = Database()

#         self.initUI()
#         self.show()

#     def initUI(self):
#         self.v_box = QVBoxLayout()
#         self.h_box = QHBoxLayout()

#         self.model = QStandardItemModel()
#         self.model.setHorizontalHeaderLabels(['Id', "Name", 'Author', 'Genre', 'Quantity'])

#         self.Add_data_to_table(self.core.get_all_books())

#         self.table_view = QTableView()
#         self.table_view.setModel(self.model)
#         self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.v_box.addWidget(self.table_view)

#         self.update_book_btn = Button("Update")
#         self.delete_book_btn = Button("Delete")
#         self.add_book_btn = Button("Add book")

#         # self.h_box.addStretch(5)
#         self.h_box.addWidget(self.update_book_btn)
#         # self.h_box.addStretch(5)
#         self.h_box.addWidget(self.delete_book_btn)
#         # self.h_box.addStretch(5)
#         self.h_box.addWidget(self.add_book_btn)
#         # self.h_box.addStretch(5)

#         self.v_box.addLayout(self.h_box)

#         self.setLayout(self.v_box)

#     def Add_data_to_table(self, books: list):

#         self.model.setRowCount(len(books))

#         for row, item_data in enumerate(books):
#             print(row)
#             print(item_data)
#             for i in range(len(item_data)):
                # self.model.setItem(row, i, QStandardItem(str(item_data[i])))