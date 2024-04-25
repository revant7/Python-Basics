#menu-driven program of binary files.
#(Running all operations in one file)
import B1,B2,B3,B4,B5
def Menu():
    a =(
"""**********MENU**********
Enter :-
1 Add New Records
2 Display All Records
3 Display Specific Records
4 Modify Records
5 Delete Records
6 Exit

***************************""")
    print(a)
    while True:
        inp = int(input("Enter Your Choice:- "))
        if inp == 1:
            B1.addrec()
        elif inp == 2:
            B2.disp()
        elif inp == 3:
            B3.specific_disp(int(input("Enter Room Number:- ")))
        elif inp == 4:
            B4.mod(int(input("Enter Room Number:- ")))
        elif inp == 5:
            B5.Delete(int(input("Enter Room Number:- ")))
        elif inp == 6:
            print("Binary File Operations Are Over.")
            break
        else:
            print("Invalid Input! Enter Correct Choice.")
            print(a)
            
Menu()
