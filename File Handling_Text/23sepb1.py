import pickle as p

def cf():
    f = open("b.dat","ab")
    rec = [3,"Ip",625]
    p.dump(rec,f)
    f.close()

def rf(bn):
    f = open("b.dat","rb")
    n = 0
    try:
        while True:
            rec = p.load(f)
            if bn == rec[0]:
                n += 1
                print(rec)

    except:
        f.close()
        return n
    

cf()
print(rf(2))
