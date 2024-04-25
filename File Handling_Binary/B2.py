#2.write a function disp() to display all records

import pickle as pk
a = """
========== Record {} ==========

Room Number:- {}
Room Price:- ₹{}
Room Type:- {}
Room Rating:- {}

============================"""
def disp():
    file = open("data.dat","rb")
    global a
    try:
        rec_no = 0
        while True:
            rec = pk.load(file)
            rec_no += 1
            print(a.format(rec_no,rec[0],rec[1],rec[2],rec[3]))
    except:
        file.close()


