import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,  # Use the port shown in DBngin
    user="root",
    password="your_password",  # Enter the password shown in DBngin
    database="your_db"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")

for table in cursor:
    print(table)

conn.close()
