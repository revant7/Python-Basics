import pickle
def createfile():
    f = open("Book.dat","ab")
    b_no = int(input("Enter Book Number : "))
    b_name = input("Enter Book Name : ")
    b_price = int(input("Enter Book Price : "))
    rec = [b_no,b_name,b_price]
    pickle.dump(rec,f)
    f.close()

createfile()

def countrec(b_no):
    f = open("Book.dat","rb")
    num = 0
    try:
        while True:
            rec = pickle.load(f)
            if b_no == rec[0]:
                num += 1
                print(rec[0],rec[1],rec[2])
    except:
        f.close()
        return num

n = countrec(int(input("Enter Book Number : ")))
print("The Number Of Records Are : ",n)
    
    
