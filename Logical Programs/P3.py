#write a program in python to count frequency of
#each vowel in a file "data.txt"

a,e,i,o,u = 0,0,0,0,0
file = open("data.txt","r")
c = file.read()
for ch in c:
    if ch.lower() == "a":
        a += 1
    elif ch.lower() == "e":
        e += 1
    elif ch.lower() == "i":
        i += 1
    elif ch.lower() == "o":
        o += 1
    elif ch.lower() == "u":
        u += 1

print("Frequency of a:-",a)
print("Frequency of e:-",e)
print("Frequency of i:-",i)
print("Frequency of o:-",o)
print("Frequency of u:-",u)

file.close()
