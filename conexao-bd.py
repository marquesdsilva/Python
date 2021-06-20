import mysql.connector
meudb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="828706",
    database="dbteste"
)
meucursor = meudb.cursor()

#sql = "INSERT INTO cliente (name, address) VALUES (%s, %s)"
#val = ("Renato", "Rua do carmo")
meucursor.execute("SELECT * FROM cliente")
meuresultado= meucursor.fetchall()


#meudb.commit()

#print(meucursor.rowcount, "record inserted.")

for x in meuresultado:
     print(x)



