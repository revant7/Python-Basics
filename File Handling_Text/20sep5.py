def countmemy():
    s = 0
    f = open("ex5.txt","a")
    for i in range(2):
        a = input(f"Enter Line {i}: ")
        f.write(a)
    f.close()

    f = open("ex5.txt","r")
    c = f.read()
    for i in range(1,len(c)):
        if (c[i-1]+c[i]).lower() in ["me","my"]:
            s += 1

    return s

print(countmemy())
        
    
