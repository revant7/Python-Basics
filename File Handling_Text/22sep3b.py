import pickle as p

def addrec():
    f = open("data1.dat","ab")
    rn = int(input("Enter Room Number: "))
    pr = float(input("Enter Price Of The Room: "))
    rt = input("Enter Type Of The Room: ")
    rec = [rn,pr,rt]
    p.dump(rec,f)
    print("Record Added Successfully.")

def disp():
    f = open("data1.dat","rb")
    try:
        i = 0
        while True:
            i += 1
            rec = p.load(f)
            print(f"Record {i}: {rec}")
    except:
            f.close()
            print("That's It.")

def specific_disp(rn):
    f = open("data1.dat","rb")
    try:
        while True:
            d = p.load(f)
            if rn == d[0]:
                print(f"Record Found: {d}")

    except:
        f.close()

def mod(rn):
    import os
    f = open("data1.dat","rb")
    f1 = open("data2.dat","wb")
    try:
        while True:
            d = p.load(f)
            if rn != d[0]:
                p.dump(d,f1)
            

            elif rn == d[0]:
                print("Record Found.")
                print(f"Old Record: {d}")
                r = int(input("Enter Updated Room Number: "))
                pr = float(input("Enter Updated Price: "))
                rt = input("Enter Updated Room Price: ")
                rec = [r,pr,rt]
                p.dump(rec,f1)
                print("Record Updated Successfully.")
    except:
        f.close()
        f1.close()
        os.remove("data1.dat")
        os.rename("data2.dat","data1.dat")
    

disp()            
mod(6)

f = open("data1.dat","rb")
while True:
        d = p.load(f)
        print(d)

f.close()









    
    
    
    
    
