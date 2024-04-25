
n = []
s = []
o = [1, 2, 3, 4]
d = {}

print('-'*12,"OPTIONS",'-'*12)

print('Type \"1\" To Add Employee Details')
print('Type \"2\" To View Employee Details')
print('Type \"3\" To Search From Employee Details')
print('Type \"4\" To Delete Employee Details')
print('Type \"9\" To Quit.')

print('-'*31)

c = int(input('Enter Your Choice : '))

if c == 1:
    n1 = input('Enter Employee Name: ')
    s1 = input('Enter Employee Salary: ')

    n.append(n1)
    s.append(s1)

    d[n] = s

    print('Employee Detail Added Successfully!')

elif c == 2:
    print(d)

elif c == 3:
    pass

elif c == 4:
    pass

elif c == 9:
    quit()

else:

    print('ERROR')
    
    
