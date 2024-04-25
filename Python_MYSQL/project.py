#importing required modules
import mysql.connector as sqlc
import random,string,time
from datetime import datetime
#establishing connection to MySql
c = sqlc.connect(username="root",host="localhost",passwd="root",database="ABCBank")
cur = c.cursor()
#Main menu
def Main_Menu():
    print("-----------------------Welcome To ABCBank------------------------")
    print("\nEnter: ")
    print("\n\t1: To Create New Account")
    print("\n\t2: To Login To Existing Account")
    print("\n\t3: For Permanent Closure of Account")
    print("\n\t4: To Exit\n")
#required functions
def custid(): #to create random customer id
    res1 = "".join(random.choices(string.ascii_uppercase,k=4))
    res2 = "".join(random.choices(string.digits,k=4))
    res = res1 + res2
    return res
def accno(): #to create a random account number
    no = "".join(random.choices(string.digits,k=6))
    no = "1210000085" + no
    no = int(no)
    return no
def transid(): #to create a random transaction id
    no = "".join(random.choices(string.digits,k=12))
    return no
##############################Execution########################################
while True:
    Main_Menu()
    choice = int(input("\nEnter Your Choice:- "))
#######################Choice 1#########################
    if choice == 1:
        #taking info from user
        name = input("Enter Your Name:- ")
        gen = input("Gender:- ")
        typ = input("Enter Type of Acc You want to open:- ")
        pin = int(input("Set Your Pin:- "))
        pinc=int(input("Confirm Your Pin:- "))
        cust_id = custid()
        acc_no = accno()

        #checking necessary values
        while pin != pinc:
            print("Pin Does Not Match!")
            pin = int(input("Set Your Pin:- "))
            pinc=int(input("Confirm Your Pin:- "))

        cur.execute("select Customer_ID from cd")
        ids = cur.fetchall()
        for i in ids:
            while cust_id in i:
                cust_id = custid()

        cur.execute("select Account_Number from cd")
        accnos = cur.fetchall()
        for i in accnos:
            while acc_no in i:
                acc_no = accnos()

        q = f"insert into cd values('{cust_id}','{name}','{gen}',{acc_no},'{typ}',{pin},{0})"
        cur.execute(q)
        c.commit()
        print("Account Created Successfully")
        cur.execute(f"select * from cd where Customer_ID='{cust_id}'")
        print("\nPlease Note Your Account Details Carefully And Don't Share It With Anyone.\n")
        print("\n*****************************************************************************************\n")
        d=cur.fetchall()
        for i in d:
            print("Customer ID:-" ,i[0])
            print("Account Name:-" ,i[1])
            print("Gender:-" ,i[2])
            print("Account Number:-" ,i[3])
            print("Account Type" ,i[4])
            print("Balance:-" ,i[6])
        print("\n*****************************************************************************************\n")
##########################Choice 2#########################
    elif choice == 2:
        while True:
            cid = input("\nEnter Your Customer ID :- ")
            pinn = int(input("Enter Your Pin :- "))
            cur.execute(f"select * from cd where Customer_ID = '{cid}' and Pin = {pinn}")
            data = cur.fetchall()
            if len(data) == 0:
                print("Invalid Customer ID or Pin!")
                continue
            print(f"Welcome {data[0][1]},\n")
            print("Enter:- ")
            print("1 To Add Money")
            print("2 For Online Money Transfer")
            print("3 To Display Transaction History")
            print("4 To Download Transaction History")
            print("5 To Withdraw Money")
            print("6 To Exit")

            ch = int(input("Enter Your Choice:- "))
            if ch == 1:
                mon = int(input("Enter Amount To Add In Account:- "))
                cur.execute(f"update cd set Balance = Balance + {mon} where Customer_ID = '{cid}'")
                cur.execute("select Transaction_ID from trans")
                transids = cur.fetchall()
                trans_id = transid()
                while trans_id in transids[0]:
                    trans_id = transid()
                cur.execute(f"insert into trans values ('{cid}','{trans_id}','{str(datetime.now())}',{mon},'CREDIT')")
                print("Amount Added Successfully.")
                cur.execute(f"select Balance from cd where Customer_ID = '{cid}'")
                print(f"Updated Balance = {cur.fetchall()[0][0]}")
                c.commit()
                continue
            elif ch == 2:
                acc2 = int(input("Enter Payee Account Number:- "))
                amt2 = float(input("Enter Amount To Be Transferred:- "))
                pin2 = int(input("Enter Your Account Pin To Confirm Transaction:- "))
                cur.execute(f"select * from cd where Customer_ID = '{cid}' and Pin = {pin2}")
                dat = cur.fetchall()
                if len(dat) != 0:
                    cur.execute("select Account_Number from cd")
                    dat2 = cur.fetchall()
                    while acc2 not in dat2[0]:
                        print("Account with this Account Number Does Not Exists.")
                        print("Enter Again. or enter 0 to Cancel Transaction")
                        acc2 = int(input("Enter Payee Account Number:- "))
                        if acc2 == 0:
                            break
                    cur.execute(f"select Balance from cd where Customer_ID = '{cid}'")
                    dat4 = cur.fetchall()
                    while amt2 > dat4[0][0]:
                        print("Low Balance In Your Account.")
                        print("Enter Amount Again or enter 0 to Cancel Transaction.")
                        amt2 = float(input("Enter Amount To Be Transferred:- "))
                        if amt2 == 0:
                            break
                    cur.execute(f"update cd set Balance = Balance - {amt2} where Customer_ID='{cid}'")
                    cur.execute(f"update cd set Balance = Balance + {amt2} where Account_Number={acc2}")
                    cur.execute("select Transaction_ID from trans")
                    transids = cur.fetchall()
                    trans_id = transid()
                    while trans_id in transids[0]:
                        trans_id = transid()
                    cur.execute(f"insert into trans values ('{cid}','{trans_id}','{str(datetime.now())}',{amt2},'DEBIT')")
                    cur.execute(f"select Customer_ID from cd where Account_Number = {acc2}")
                    dat6 = cur.fetchall()[0][0]
                    cur.execute("select Transaction_ID from trans")
                    transids = cur.fetchall()
                    trans_id = transid()
                    while trans_id in transids[0]:
                        trans_id = transid()
                    cur.execute(f"insert into trans values ('{dat6}','{trans_id}','{str(datetime.now())}',{amt2},'CREDIT')")
                    c.commit()
                
                    

                    
                
        
        
    
    
    
    
