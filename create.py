from connect import *

#CREATE
nome = "arroz"
valor = 30.8

sql = f'INSERT INTO produtos(nome, valor) VALUES ("{nome}", "{valor}")'
cursor.execute(sql)
connection.commit()


cursor.close()
connection.close()