#write a program to display longest word from file "data.txt"

file = open("data.txt","r")
content = file.read()
words = content.split()
for i in words:
    for j in words:
        if len(i)<len(j):
            break
    else:
        print("Longest Word Is:-",i)

            
