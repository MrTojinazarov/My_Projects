import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mr2344',
            database = 'BlogPost'
        )

    
    def Insert_user(self, user: dict):
        super().__init__()
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO Users(person, phone, login, password) VALUES (%s, %s, %s, %s);"
                cursor.execute(query, (user['person'], user['phone'], user['login'], user['password']))
                self.connection.commit()
                return False
        except Error as err:
            self.connection.rollback()
            return str(err)

    def Get_user_id(self, user: dict):
        super().__init__()
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT id FROM Users WHERE login = %s and password = %s;"
                cursor.execute(query, (user['login'], user['password']))
                self.user_id = cursor.fetchone()
                return self.user_id
        except Error as err:
            return str(err)
        
    def UploadPost(self, data: dict):
        super().__init__()
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO Blog_post(login, post, datetime) VALUES (%s, %s, %s);"
                cursor.execute(query, (data['login'], data['post'], data['datetime']))
                self.connection.commit()
                return False
        except Error as err:
            self.connection.rollback()
            return str(err)        
        
    
    def Get_own_data(self, login: str):
        super().__init__()
        try:
            with self.connection.cursor() as cursor:
                query = "select * from Blog_post Where login = %s;"
                cursor.execute(query, (login,))
                self.own_post = cursor.fetchall()
                return self.own_post
        except Error as err:
            return str(err)
        
    def Get_all_posts(self):
        super().__init__()
        try:
            with self.connection.cursor() as cursor:
                query = "select * from Blog_post;"
                cursor.execute(query)
                self.all_post = cursor.fetchall()
                return self.all_post
        except Error as err:
            return str(err)       