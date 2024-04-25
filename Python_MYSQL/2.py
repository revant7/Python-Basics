import mysql.connector as sqlc
import time,datetime
import random

c = sqlc.connect(
    host = "localhost",
    user = "root",
    password="root",
    database="shop"
    )

if c.is_connected():
    time.sleep(1)
    print("Interface Connected To Server Successfully.")
    time.sleep(1)
    print("Welcome.\n")
else:
    print("Error connecting to server. Please try again later.")

name = input("Enter Your Name:- ")

cursor = c.cursor()
cursor.execute("select * from Customers")
cust_data = cursor.fetchall()

for i in cust_data:
    cust_id = i[0]
    if i[1] == name:
        print("Welcome Back",name)
        print("Your Customer Id",i[0])
        break
else:
    cust_id = data[-1][0] + 1
    q = "insert into Customers values({},'{}')".format(cust_id,name)
    cursor.execute(q)
    c.commit()
    print("You Are A New Customer.")
    print("Thank You For Joining Us.")
    print("Your Customer Id Is",cust_id)

print("\nPlease Select From Our Wide Range Of Products,")

cursor.execute("select * from products_info")
data = cursor.fetchall()

for i in data:
    if i[3] > 0:
        print(i[1],"    ",i[2],"\n")

bill=[]
print("Enter Product Name, \nPress 0 To Exit")

while True:
    a = input("Enter Product Name:- ")
    if a == "0":
        break
    else:
        bill.append(a)
    
amount = 0
for i in bill:
    for j in data:
        if j[1] == i:
            amount += j[2]

print(bill)
print("Total Amount:- ",amount)
bills_str = ""
for i in bill:
    bills_str += str(i)
    bills_str += ","
for i in bill:
    cursor.execute("update products_info set Available_Qty = Available_Qty - 1 where Product_Name = '{}'".format(i))
    c.commit()
cursor.execute("insert into bills values ({},'{}','{}',{},{})".format(cust_id,str(datetime.datetime.now()),bills_str,0,amount))
c.commit()

        

