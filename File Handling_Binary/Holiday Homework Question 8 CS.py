def countmy()
    with open("STORY.txt","r") as f:
        c = 0
        mc = 0
        a = f.read()
        for i in range(0,len(a)-1):
            b = a[i]+a[i+1]
            if b in ["My"]:
                c += 1
            if b in ["my"]:
                mc += 1

        print("Count Of My:",c)
        print("Count Of my:",mc)
    

    f.close()
countmy()     
    
