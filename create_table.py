import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Myselfs@1',database='Inventory_Management')
cur=mydb.cursor()
 
 # Create the 'manufacture' table
cur.execute('CREATE TABLE manufacture (manufacture_id INTEGER PRIMARY KEY, item_name VARCHAR(20),company varchar(20),item_color VARCHAR(20),quantity INTEGER(4),defective_items INTEGER(4))')

# Create the 'goods' table
cur.execute('CREATE TABLE goods (goods_id INTEGER(4) PRIMARY KEY, manufacture_id INTEGER, manufacture_date DATE,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))')

# Create the 'purchase' table
cur.execute('CREATE TABLE purchase (purchase_id INTEGER(4) PRIMARY KEY,  store_name varchar(20),purchase_amount FLOAT, purchase_date DATE)')

# Create the 'sale' table
cur.execute('CREATE TABLE sale (sale_id INTEGER(4) PRIMARY KEY,store_name VARCHAR(30),sale_date DATE,goods_id INTEGER(4), profit_margin FLOAT,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))')

