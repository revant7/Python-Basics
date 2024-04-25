#removing repeted lines
with open("star.txt","r") as f:
    c = f.readlines()
    l = []
    for i in c:
        if i not in l:
            l.append(i)



with open("star.txt","w") as f:
    for i in l:
        f.write(i)

print(l)
