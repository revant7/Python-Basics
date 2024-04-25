import time
import functions as f
print("""
Enter :
0 To Exit The File Handler
1 To Create A File
2 To Open A File
3 To Read A File
4 To Write In A File
5 To Append In A File
6 To Calculate Size Of a File
7 To Delete A File
8 To Create a Copy Of a File
9 To Use Binary Operations""")

file_n = input("Enter File Name On Which Operations To Be Done : ")
choice = input("Enter Your Choice : ")

while True:
    if int(choice)>0 and int(choice)<10:
        if choice == "1":
            name = input("Enter The Name Of File To Be Created : ")
            f.file_creator(name)
            choice = input("Enter Your Choice : ")
        elif choice == "2":
            file_mode = input("Enter File mode: ")
            f.file_opener(file_n,file_mode)
            choice = input("Enter Your Choice : ")
        elif choice == "3":
            char = input("No. of Chracters To Be Displayed [ for all press '*' ] : ")
            f.file_reader(char)
            choice = input("Enter Your Choice : ")
        elif choice == "4":
            txt = input("Enter Text : ")
            f.file_writer(txt)
            choice = input("Enter Your Choice : ")
        elif choice == "5":
            text = input("Enter The Text To Be Added In The File: ")
            file.appender(text,file_n)
            choice = input("Enter Your Choice : ")
        elif choice == "6":
            f.file_size(file_n)
            choice = input("Enter Your Choice : ")
        elif choice == "7":
            name = input("Enter The Name Of File To Be Deleted: ")
            f.file_delete(name)
            choice = input("Enter Your Choice : ")
        elif choice == "8":
            pass
        elif choice == "9":
            pass
    elif choice == "0":
        print("Program Will Break In 3 Sec")
        time.sleep(3)
        break
    
    else:
        print("Please Enter a Valid Input")
        choice = input("Enter Your Choice : ")

        
        
    
    
    
            


        
