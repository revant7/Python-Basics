#def a function to check that a number/word is palindrome or not
#palindrome means something is equals to reverse of itself

def Palindrome(p):
    pn = str(p.lower())
    r = pn[::-1]
    if pn == r:
        return f"{p} Is A Palindrome."
    else:
        return f"{p} Is Not A Palindrome."
    
        
p = input("Enter a word or a number:- ")
print(Palindrome(p))
