import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mr2344',
            database = 'market'
        )

    def get_user_id(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT id FROM users WHERE login = %s and password = %s;"
                cursor.execute(query, (user['login'], user['password']))
                self.id_ = cursor.fetchone()
                return self.id_
        except Error as err:
            return str(err)
        

    def add_user_data(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO users(login, password) VALUES (%s, %s);"
                cursor.execute(query, (user['login'], user['password']))
                self.connection.commit()
                return False
        except Error as err:
            return str(err)        
        

    def get_all_items(self):
        try:
            with self.connection.cursor() as cursor:
                query = "select * from items;"
                cursor.execute(query)
                self.all_items = cursor.fetchall()
                return self.all_items
        except Error as err:
            return str(err)    
        

    def Update_item(self, data: dict):
        try:
            with self.connection.cursor() as cursor:
                query = """
                Update items
                Set item = %s, price = %s, quantity = %s
                where id = %s;"""
                cursor.execute(query, (data['item'], data['price'], data['quantity'], data['id']))
                self.connection.commit()
                return None
        except Error as err:
            self.connection.rollback()
            return str(err)
        
    # def delete_item(self, id: str):
    #     try:
    #         with self.connection.cursor() as cursor:
    #             query = "Delete from items where id = %s"