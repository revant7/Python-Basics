f = open("ex3.txt","w")
f.write("Hello")
f.write("\nMy Name Is ")
f.write("\nRevant")
f.write("\nI Love Coding...")
f.close()

with open ("ex3.txt", "r") as f:
    for i in f.readlines():
        print(i[::-1])
    
    
