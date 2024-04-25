import csv
with open("data.csv","w") as f:
    w = csv.writer(f)
    w.writerow(["Roll No.", "Name", "Marks"])

    for i in range(5):
        while True:
            try:
                print("Student Record :", (i + 1))
                rno = int(input("Enter Roll Number : "))
                name = input("Enter Your Name : ")
                marks = float(input("Enter Your Marks : "))
                rec = [rno,name,marks]
                w.writerow(rec)
        
            except Exception as e:
                print(e)
                continue

            break

f.close()
