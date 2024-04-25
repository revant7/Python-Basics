#3.write a function specific_disp(room_no) which takes room_no
#as argument and display its details.
import pickle as pk
a = """
========== Record {} ==========

Room Number:- {}
Room Price:- ₹{}
Room Type:- {}
Room Rating:- {}

============================"""
def specific_disp(room_no):
    file = open("data.dat","rb")
    global a
    try:
        rec_no = 0
        while True:
            rec = pk.load(file)
            rec_no += 1
            if room_no == rec[0]:
                print(a.format(rec_no,rec[0],rec[1],rec[2],rec[3]))
    except:
        file.close()













