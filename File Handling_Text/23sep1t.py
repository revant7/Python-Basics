f = open("star.txt","r")
l = f.readlines()
for i in l:
    for j in l:
        if len(i) < len(j):
            break
    else:
        print(i)
    
