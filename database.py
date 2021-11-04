import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection
from flask_mysqldb import MySQL

def connect():
    mes = "Success"
    mes1 = "Fail"
    con = None
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM demo")
            row = cursor.fetchone()
            str = ''
            for i in row:
                str = str + i
            print(str)
            return str
    except Error as e:
        return mes1

