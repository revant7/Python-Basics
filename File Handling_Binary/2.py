import pickle
f = open("Student.dat","wb")
a=[[1,"Revant",99],[2,"Yash",95],[3,"Shreshth",85],[4,"Rohan",90]]
for i in a:
    pickle.dump(i,f)
f.close()
def countrec():
    f = open("Student.dat","rb")
    c = 0
    try:
        while True:
            data = pickle.load(f)
            if data[2] >= 90:
                c += 1
                print(data)
    except:
        print(c)
        f.close()

countrec()
