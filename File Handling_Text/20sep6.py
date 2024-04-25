s = 0
f = open("ex5.txt","r")
c = f.read()
l = c.split()
for i in l:
    if i.lower() == "my" or i.lower() == "me":
        s += 1

print(s)
f.close()
