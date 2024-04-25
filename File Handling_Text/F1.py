#write a program to display factorial of a number

def Factorial(n):
    f = 1
    for i in range(2,n+1):
        t = f * i
        if i == 2:
            f = 0
            f += t
        else:
            f = t
    return f

n = int(input("Enter A Number: "))
if (n == 0) or (n == 1): 
    print(f"Factorial of {n} is 1.")
else:
    print(f"Factorial of {n} is {Factorial(n)}.")

