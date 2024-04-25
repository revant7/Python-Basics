def line_counter(name = "STORY.txt"):
    c = 0
    with open(name,"r") as f:
        for i in f.readlines():
            c += 1    
        print("The Number Of Lines In File Is : ",c)
    f.close()
line_counter()
