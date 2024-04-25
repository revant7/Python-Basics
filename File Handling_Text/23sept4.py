#to remove duplicate lines
with open("star.txt","r") as f:
    c = f.readlines()

    for i in c:
        if c.count(i) > 1:
            c.remove(i)


str1 = ""
for i in c:
    str1 += i

with open("star.txt","w") as f:
    f.write(str1)


    
