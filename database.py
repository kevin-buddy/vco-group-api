import mysql.connector
from dotenv import load_dotenv
import os

class MySQL:
    def __init__(self):
        self.cnx = None
        self.config = {
            'user': os.getenv("DATABASE_USER"),
            'password': os.getenv("DATABASE_PASSWORD"),
            'host': os.getenv("DATABASE_HOST"),
            'database': os.getenv("DATABASE"),
            'raise_on_warnings': True
        }

    def get_db_cursor(self):
        self.cnx = mysql.connector.connect(**self.config)
        return self.cnx.cursor()
    def close_db(self):
        self.cnx.close()
    def get_customers(self):
        cursorObject = self.get_db_cursor()
        
        query = "SELECT * FROM customers LIMIT 2 OFFSET 1"
        cursorObject.execute(query)
        
        myresult = cursorObject.fetchall()
        self.close_db()
        return myresult