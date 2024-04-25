with open("abc.txt","w") as f:
    f.write("Python Is an object oriented programming language.")
    f.seek(10)
    f.write("Bhumi")
    
    f.close()
with open("abc.txt","r") as f:
    a = f.read(4)
    b = f.read(5)
    print(f.seek(2))
    
    c = f.read(3)
    
    print(a)
    print(b)
    print(c)
    print("Cursor Position ",f.tell())
    print(f.read())
    f.close()

    
