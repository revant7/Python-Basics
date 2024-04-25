import pickle,os
def Delete(room_no):
    try:
        file = open("data.dat","rb")
        f = open("temp.dat","wb")
        while True:
            rec = pickle.load(file)
            if room_no != rec[0]:
                pickle.dump(rec,f)
    except:
        print("Record Deleted Successfully.")
        file.close()
        f.close()
        os.remove("data.dat")
        os.rename("temp.dat","data.dat")


