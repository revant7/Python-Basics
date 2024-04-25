#display unique words
with open("star.txt","r") as f:
    c = f.read()
    l = c.split()
    uw = []
    for i in l:
        if i not in uw:
            uw.append(i)

    print(uw)
