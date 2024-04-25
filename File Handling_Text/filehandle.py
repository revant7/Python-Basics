import csv

f = open("dialogs.txt","r")
f1 = open("dialogs.csv","a",newline = "")

w = csv.writer(f1,delimiter = ",")
w.writerow(["Ques","Ans"])

c = f.read()
c = c.split("\n")

for i in c:
    rec = i.split("\t")
    w.writerow([rec[0],rec[1]])

f1.close()
f.close()

f = open("dialogs.csv","r",newline="\r\n")
r = csv.reader(f)
z = 0
for i in r:
    z += 1
    print(i)
    if z>5:
        break
f.close()
   
