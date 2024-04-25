def writer(w,s=0):
    f = open("2121.txt","a")
    f.seek(s)
    f.write(w)
    f.close()

def reader():
    f = open("2121.txt","r")
    print(f.read())
    f.close()


writer("My Name is Revant")
reader()
