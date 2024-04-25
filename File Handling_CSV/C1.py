#adding records in csv file and calculating percentage
import csv
with open("data.csv","w") as file:
    w = csv.writer(file,delimiter=",")
    w.writerow(["Admission Number","Name","Physics","Chemistry","Maths","Cs","Percentage"])
    while True:
        adm = int(input("Enter Your Admission Number:- "))
        n = input("Enter Name:- ")
        p = float(input("Enter Your Physics Marks:- "))
        c = float(input("Enter Your Chemistry Marks:- "))
        m = float(input("Enter Your Maths Marks:- "))
        cs = float(input("Enter Your Computer Science Marks:- "))
        a = (p+c+m+cs)/400
        a = a * 100
        w.writerow([adm,n,p,c,m,cs,int(a)])
        inp = input("Do you want to enter more records? [Y/n]:- ")
        if inp.lower() == "n":
            break

        
