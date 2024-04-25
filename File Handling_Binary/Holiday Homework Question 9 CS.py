def words_counter():
    with open("STORY.txt","r") as f:
        a = f.readlines()
        c = 0
        for i in a:
            x = i.split(" ")
            c = c + len(x)
        print("Number Of Words In File Is:",c)

words_counter()
