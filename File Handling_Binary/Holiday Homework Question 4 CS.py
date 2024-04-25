def displaywords():
    with open("STORY.txt","r") as f:
        content = f.read()
        lst = content.split()
        for i in lst:
            j = list(i)
            if len(j) < 4:
                print(i)

displaywords()
