#to modify record in a csv file
#using admission number
import csv,os
inp = int(input("Enter Admission Number:- "))
f1 = open("data.csv","r",newline="\r\n")
f2 = open("temp.csv","w",newline="\r\n")
r = csv.reader(f1)
w = csv.writer(f2)
for i in r:
    if inp == int(i[0]):
        i[2] = float(input("Enter Your Physics Marks:- "))
        i[3] = float(input("Enter Your Chemistry Marks:- "))
        i[4] = float(input("Enter Your Maths Marks:- "))
        i[5] = float(input("Enter Your Computer Science Marks:- "))
        i[6] = (i[2]+i[3]+i[4]+i[5])/400
        i[6] = i[6] * 100
    w.writerow([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
print("Data Updated Successfully.")
f1.close()
f2.close()
os.remove("data.csv")
os.rename("temp.csv","data.csv")

        
