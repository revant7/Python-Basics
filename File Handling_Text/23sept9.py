with open("star.txt","r") as f:
    t = 0
    m = 0
    c = f.readlines()
    for i in c:
        if i[0] in ["M","m"]:
            m += 1
        elif i[0] in ["T","t"]:
            t += 1
    print("M: ",m)
    print("T: ",t)
            
