def COUNTAE():
    f = open("star.txt","r")
    c = f.readlines()
    for i in c:
        if i[0] in ["A","E"]:
            print(i)

    f.close()

COUNTAE()

def COUNTAE1():
    f = open("star.txt","r")
    c = f.readlines()
    while c:
        print("=")
        if c[0] in ["A","E"]:
            print(c)

        else:
            continue
        print("Error")
    print("Closed")
    f.close()

COUNTAE1()
    
