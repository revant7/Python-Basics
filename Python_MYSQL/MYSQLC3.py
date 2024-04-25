#program to update a table
import mysql.connector as sqlc
c = sqlc.connect(
    host = "localhost",
    user = "root",
    password="root",
    database="shop"
    )
cur = c.cursor()

q = "update products_info set Available_Qty = 0 where Product_ID<5"
cur.execute(q)
c.commit()
cur.execute("select * from products_info")
data = cur.fetchall()

for i in data:
    print(i,"\n")

c.close()
