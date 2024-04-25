myvalue = []
def push(n):
    myvalue.append(n)
    print(myvalue)

push(1)
push(2)
push(3)
push(7)

def pop():
    print(f"Element {myvalue.pop()} Removed Successfully.")
    print(myvalue)

pop()
pop()

myvalue1 = []

def R_push(n):
    if len(myvalue1) < 3:
        myvalue1.append(n)
        print(myvalue1)
    else:
        raise ValueError("Stack Is Full ! ")
R_push("Revant")
R_push("Shreshth")
R_push("Rohan")
R_push("Yash")






        
    
