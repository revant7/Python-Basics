#to display all records from csv file
import csv
with open("data.csv","r",newline="\r\n") as file:
    r = csv.reader(file)
    for i in r:
        print(i)
    
