#program to show records from table
import mysql.connector as sqlc
c = sqlc.connect(
    host = "localhost",
    user = "root",
    password="root",
    database="shop"
    )
cur = c.cursor()

cur.execute("select * from products_info")

data = cur.fetchall()

print("Records of table products_info are:- \n")

for i in cur.description:
    print(i[0],end=", ")
print("\n")

for i in data:
    print(i,"\n")

c.close()
