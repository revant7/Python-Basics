f = open("star.txt","r")
c = f.read()
l = c.split()
for i in l:
    for j in l:
        if len(i)<len(j):
            break
    else:
        print(i)
                      
