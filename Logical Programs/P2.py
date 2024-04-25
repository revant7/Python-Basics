#write a program to display unique words from file "data.txt"

with open("data.txt","r") as file:
    c = file.read()
    l = c.split()
    ul = []
    for i in l:
        if i not in ul:
            ul.append(i)
    print(ul)
        
    
