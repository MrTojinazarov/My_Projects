import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mr2344',
            database = 'product_list'
        )

    def Insert_User(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""
                    INSERT INTO products(login, password)
                    VALUES ('{user['login']}', '{user['password']}');
                """)
                self.connection.commit()
                return False
        except Error as err:
            return str(err)


    def get_user_data(self, user: dict):
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT id FROM products WHERE login = %s and password = %s;"
                cursor.execute(query, (user['login'], user['password']))
                self.id_ = cursor.fetchone()
                return self.id_
        except Error as err:
            return str(err)
        