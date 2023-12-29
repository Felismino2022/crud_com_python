from connect import *

#READ
sql = 'SELECT *FROM produtos'
cursor.execute(sql)
resultado = cursor.fetchall()
print(resultado)


cursor.close()
connection.close()