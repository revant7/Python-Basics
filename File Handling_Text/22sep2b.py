f = open("ex12","a+")



f.write("My NAme IS ")
f.seek(0)
print(f.read())                                     
f.close()
