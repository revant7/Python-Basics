def RevText():
    with open("STORY.txt","r") as f:
        content = f.read()
        lst = content.split()
        for i in lst:
            if i[0] in ["i","I"]:
                lst1 = list(i)
                lst1.reverse()
                new_str = ""
                for j in lst1:
                    new_str = new_str + j
                lst[lst.index(i)] = new_str
        print(lst)



RevText()
                    
