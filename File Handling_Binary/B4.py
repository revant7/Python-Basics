#write a function mod(room_no) which takes room_no as
#argument and modify its details.
import pickle,os
def mod(room_no):
    try:
        file = open("data.dat","rb")
        temp = open("temp.dat","wb")
        while True:
            rec = pickle.load(file)
            if room_no == rec[0]:
                rec[1] = float(input("Enter Modified Room Price:- "))
                rec[2] = input("Enter Modified Room Type:- ")
                rec[3] = int(input("Enter Modified Room Rating:- "))
            pickle.dump(rec,temp)
    except:
        print("Record Modified Successfully.")
        file.close()
        temp.close()
        os.remove("data.dat")
        os.rename("temp.dat","data.dat")


