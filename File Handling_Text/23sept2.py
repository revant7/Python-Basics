with open("star.txt","r") as f:
    c = f.readlines()
    for i in c:
        if len(i) > 40:
            print(i)

