import pickle
def CreateFile():
    f = open("Book.dat","ab")
    bno = int(input("Enter Book Number:- "))
    bname = input("Enter Book Name:- ")
    ba = input("Enter Book Author:- ").title()
    bp = float(input("Enter Book Price:- "))
    rec = [bno,bname,ba,bp]
    pickle.dump(rec,f)
    f.close()

def CountRec(a):
    a = input("Enter Author Name:- ").title()
    f = open("Book.dat","rb")
    c = 0
    try:
        while True:
            data = pickle.load(f)
            if data[2] == a:
                c += 1
                
    except:
        print(c)
        f.close()

a = "y"
while a == "y":
    CreateFile()
    a = input("Enter y To Add more records:- ")

CountRec(1)
