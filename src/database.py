import mysql.connector
import os
from mysql.connector import Error

class MySQLConnection:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            try:
                cls._instance.connection = mysql.connector.connect(
                    host = os.getenv('HOSTNAME'),
                    user = os.getenv('USERNAME'),
                    password = os.getenv('PASSWORD'),
                    database = os.getenv('DATABASE'),
                    buffered = True
                )
                print("MySQL Database connection successful")
            except Error as err:
                print(f"Error: '{err}'")

        return cls._instance

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def drop_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS library;")
        cursor.execute("DROP TABLE IF EXISTS customer;")
        cursor.execute("DROP TABLE IF EXISTS book;")
        cursor.execute("DROP TABLE IF EXISTS author;")
        self.connection.commit()
        cursor.close()
