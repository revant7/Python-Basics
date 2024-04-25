#to display record of thoose students whoose
#percentage is greater then 90%
import csv
with open("data.csv","r",newline="\r\n") as file:
    r = csv.reader(file)
    for i in r:
        print(i)
        if type(i[6]) != type(" "):      
            if i[6] > 90:
                print(i)

        else:
                print(1)
        
        
