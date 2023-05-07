import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Myselfs@1',database='Inventory_Management')
cur=mydb.cursor()
e1='insert into manufacture(manufacture_id ,item_name ,company,item_color ,quantity ,defective_items) values (%s,%s,%s,%s,%s,%s)'
entries1 = (1, 'wooden chair','GARUD ENTERPRISES' ,'brown', 100, 0), (3, 'wooden table','SS EXPORT' 'brown', 50, 1),(2, 'red toy','F3 TOYS','red', 200, 0),(4,'shirt','ADIDAS','black',300,1)
cur.executemany(e1,entries1)
mydb.commit()
#Insert multiple entries to the 'goods' table
e2='insert into goods(goods_id , manufacture_id , manufacture_date)values (%s,%s,%s)'
entries2 = (1, 1, '2023-04-20'),(2, 1, '2023-04-22'),(3, 2, '2023-04-25'),(4, 3, '2023-04-26')
cur.executemany(e2,entries2)
mydb.commit()
# Insert multiple entries to the 'purchase' table
e3='insert into purchase(purchase_id , store_name,purchase_amount,purchase_date)values(%s,%s,%s,%s)'
entries3 = (1, 'ORay', 500, '2023-04-21'), (2, 'MyKids', 1000, '2023-04-22'),(3, 'OnlineMart', 750, '2023-04-23')
cur.executemany(e3,entries3)
mydb.commit()
# Insert multiple entries to the 'sale' table
e4='INSERT INTO sale(sale_id ,store_name ,sale_date,goods_id , profit_margin )values(%s,%s,%s,%s,%s)'
entries4 = (1, 'MyCare', '2023-04-01', 1, 100),(2, 'ORay', '2023-04-03', 2, 50),(3, 'MyKids', '2023-04-05', 3, 75),(4, 'OnlineMart', '2023-04-06', 4, 80)
cur.executemany(e4,entries4)
mydb.commit()

