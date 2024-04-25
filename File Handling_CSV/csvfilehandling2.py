import csvfilehandling as csvfh
import csv
def csvreader():
    with open("data.csv","r",newline="\r\n") as f:
        r = csv.reader(f)
        for rec in r:
            print(rec)


csvreader()
