from os import close
import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection
from flask_mysqldb import MySQL
from info import  not_id, verify

def connect(id,mno):
    con = None
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT * FROM sab WHERE id='"+id+"' AND phone='"+mno+"';"
            cursor.execute(query)
            row = cursor.fetchone()
            if not row:
                mes = not_id()
                return mes
            else:
                mes = verify()
                return mes
                """string = ''
                for i in row:
                    string = string + str(i)
                return string"""
    except Error as e:
        string = "System Error"
        return string




def get_name(id,mno):
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT name FROM sab WHERE id='"+id+"' AND phone='"+mno+"';"
            cursor.execute(query)
            row = cursor.fetchone()
            string = ''
            for i in row:
                string = string + str(i)
            return string
    except Error as e:
        string = "System Error"
        return string


def get_cgpa(id,mno):
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT cgpa FROM sab WHERE id='"+id+"' AND phone='"+mno+"';"
            cursor.execute(query)
            row = cursor.fetchone()
            string = ''
            for i in row:
                string = string + str(i)
            return string
    except Error as e:
        string = "System Error"
        return string


def get_fee(id,mno):
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT fee FROM sab WHERE id='"+id+"' AND phone='"+mno+"';"
            cursor.execute(query)
            row = cursor.fetchone()
            string = ''
            for i in row:
                string = string + str(i)
            return string
    except Error as e:
        string = "System Error"
        return string


def get_att(id,mno):
    try:
        conn = mysql.connector.connect(host="localhost",database="sgp",user="root",password="")
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT attendance FROM sab WHERE id='"+id+"' AND phone='"+mno+"';"
            cursor.execute(query)
            row = cursor.fetchone()
            string = ''
            for i in row:
                string = string + str(i)
            return string
    except Error as e:
        string = "System Error"
        return string








