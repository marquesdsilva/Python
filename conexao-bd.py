import mysql.connector
meudb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="828706",
    database="dbteste"
)
meucursor=meudb.cursor()
meucursor.execute()

