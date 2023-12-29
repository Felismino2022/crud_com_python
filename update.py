from connect import *

#UPDATE
valor = 8
nome = "arroz"
sql = f'UPDATE produtos set valor = {valor} WHERE id = {1}'
cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()