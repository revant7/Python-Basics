############## Mind Reader Game #####################

s = 0
print("\n Welcome To Python MIND READER GAME! \n")
print("THINK OF A NUMBER BETWEEN 1 AND 63 AND KEEP IT IN YOUR MIND.")
print("\n I will Show You Six Cards One By One and, \n If The Number You Have Chosen Exist in a the CARD then type yes otherwis no. \n")
print(f"\n {'*'*25} CARD 1 {'*'*25} \n")

print("""
        1   3   5   7   9   13  15
        17  19  21  23  25  27  29
        31  33  35  37  39  41  43  
        45  47  49  51  53  55  57
        59  61  63  
""")

a = input("Your Number Exist In This Card :- ")
if a == 'yes':
  s += 1

print(f"\n {'*'*25} CARD 2 {'*'*25} \n")

print("""
         2  3   6   7   10   11  14
         15  18  19  22  23  26  27
         30  31  34  35  38  39  42  
         43  46  47  50  51  54  55
         58  59  62  63  
""")

b = input("Your Number Exist In This Card :- ")
if b == 'yes':
  s += 2

print(f"\n {'*'*25} CARD 3 {'*'*25} \n")

print("""
        4   5   6   7   12   13  14
        15  20  21  22  23  28  29
        30  31  36  37  38  39  44  
        45  46  47  52  53  54  55
        60  61  62  63  
""")

c = input("Your Number Exist In This Card :- ")
if c == 'yes':
  s += 4

print(f"\n {'*'*25} CARD 4 {'*'*25} \n")

print("""
      8   9   10  11  12  13  14
      15  24  25  26  27  28  29
      30  31  40  41  42  43  44  
      45  46  47  56  57  58  59
      60  61  62  63  
""")

d = input("Your Number Exist In This Card :- ")
if d == 'yes':
  s += 8

print(f"\n {'*'*25} CARD 5 {'*'*25} \n")

print("""
        16  17  18  19  20  22  23
        24  25  26  27  28  29  30
        31  48  49  50  51  52  53  
        54  55  56  57  58  59  60
        61  62  63
""")

e = input("Your Number Exist In This Card :- ")
if e == 'yes':
  s += 16

print(f"\n {'*'*25} CARD 6 {'*'*25} \n")

print("""
        32  33  34  35  36  37  38
        39  40  41  42  43  44  45
        46  47  48  49  50  51  52  
        53  54  55  56  57  58  59
        60  61  62  63  
""")

f = input("Your Number Exist In This Card :- ")
if f == 'yes':
  s += 32


print("\n \n Your Guessed Number Is : ",s)
