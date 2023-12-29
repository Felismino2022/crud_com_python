from connect import *

#DELETE
sql = f'DELETE FROM produtos WHERE id = {3}'
cursor.execute(sql)
connection.commit()


cursor.close()
connection.close()