#consider a binary file "data.dat" which stores the record
#of the Hotel in form of list containing:-
#Room_no,price,room_type,rating
#1.write a function addrec() to add record in a file
import pickle as pk
def addrec():
    try:
        file = open("data.dat","ab")
        while True:
            rno = int(input("Enter Room Number:- "))
            price = float(input("Enter Room Price:- "))
            rt = input("Enter Room Type:- ")
            rating = int(input("Enter Room Rating:- "))
            record = [rno,price,rt,rating]
            pk.dump(record,file)
            print("Record Added Successfully.")
            usr_inp = input("Do You Want To Enter More Records? [Y/n] :-")
            if usr_inp.lower() == "n":
                break
            elif usr_inp not in ["Y","n","N","y"]:
                print("Invalid Input! Enter Again.")
                usr_inp = input("Do You Want To Enter More Records? [Y/n] :-")
    except:
        print("Something Went Wrong. Try Again.")
    file.close()
               
