import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self)->None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mr2344',
            database = 'Liberary'
        )

    def get_user_id(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = "select id from users where login = %s and password = %s;"
                cursor.execute(query, (user['login'], user['password']))
                self.id_ = cursor.fetchone()
                return self.id_
        except Error as err:
            return str(err)
        

    def Insert_User(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = "Insert Into users(login, password) VALUES (%s, %s);"
                cursor.execute(query, (user['login'], user['password']))
                self.connection.commit()
                return False
        except Error as err:
            return str(err)
        


    def get_all_books(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("select * from books")
                self.all_books = cursor.fetchall()
                return self.all_books
        except Error as err:
            return str(err)
        

    def Update_book(self, data: dict):
        try: 
            with self.connection.cursor() as cursor:
                query = """
                UPDATE books
                SET name = %s, author = %s, genre = %s, quantity = %s
                WHERE id = %s;
                """
                cursor.execute(query, (data['name'], data['author'], data['genre'], data['quantity'], data['id']))
                self.connection.commit()
                return None
        except Error as err:
            self.connection.rollback()
            return str(err)
        

    def delete_book(self, id: str):
        try:
            with self.connection.cursor() as cursor:
                query = "DELETE FROM books WHERE id = %s;"
                cursor.execute(query, (id,))
                self.connection.commit()
                return None
        except Error as err:
            self.connection.rollback()
            return str(err)
        

    def Add_book(self, data: dict):
        try:
            with self.connection.cursor() as cursor:
                query = """Insert Into books(name, author, genre, quantity)
                VALUES (%s, %s, %s, %s);"""
                cursor.execute(query, (data['name'], data['author'], data['genre'], data['quantity']))
                self.connection.commit()
                return False
        except Error as err:
            return str(err)       