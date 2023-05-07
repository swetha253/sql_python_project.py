import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Myselfs@1')
print(mydb.connection_id)