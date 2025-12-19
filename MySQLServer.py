#!/usr/bin/python3
import mysql.connector

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # add password if needed
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # CLOSE CONNECTION
    try:
        cursor.close()
        connection.close()
    except Exception:
        pass
