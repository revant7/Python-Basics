#program to delete records in a table
import mysql.connector as sqlc
c = sqlc.connect(
    host = "localhost",
    user = "root",
    password="root",
    database="shop")
cur = c.cursor()
inp = int(input("Enter Product ID of the product to be Deleted:- "))
q=f"delete from products_info where Product_ID = {inp}"
cur.execute(q)
c.commit()
cur.execute("select * from products_info")
data = cur.fetchall()
for i in data:
    print(i,"\n")
c.close()


