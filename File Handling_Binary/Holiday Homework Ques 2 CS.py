with open("STORY.txt","r") as f:
    c = 0
    a = f.read()
    for i in range(0,len(a)-1):
        b = a[i]+a[i+1]
        if b.lower() == "my":
            c += 1
    print(c)

f.close()
        
    
