#write a program to count words whoose
#length is greater than 7 chracters

file = open("data.txt","r")
content = file.read()
words = content.split()
count = 0
for i in words:
    if len(i) > 7:
        count += 1
        print("\n",i)
file.close()
print(f"There are {count} words whoose length is more then 7 chracters.")
