#to replace the with them

with open("star.txt","r") as f:
    c = f.read()
    c = c.replace("the","them")

with open("star.txt","w") as f:
    f.write(c)

