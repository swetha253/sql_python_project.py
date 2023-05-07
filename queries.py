import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Myselfs@1',database='Inventory_Management')
cur=mydb.cursor()

s='DELETE FROM purchase WHERE item_name = "shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
cur.execute(s)
mydb.commit()


t='UPDATE manufacture SET quantity = 500 WHERE item_color = "red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "MyKids")'
cur.execute(t)
mydb.commit()


u='SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE item_name = "wooden chair" AND manufacture_date< "2023-05-01"'
cur.execute(u)
rows=cur.fetchall()
for i in rows:
    print(i)
mydb.commit()

v='SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE item_name = "wooden table" AND store_name = "MyCare",company = "SS Export"'
cur.execute(v)
row = cur.fetchone()
print(row[0])
mydb.commit()