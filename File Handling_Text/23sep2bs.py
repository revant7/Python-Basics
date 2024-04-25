l = [16,14,25,2,5,7,15,8,20,18]
print(l)
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]

print(l)
