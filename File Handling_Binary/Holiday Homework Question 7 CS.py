def I_M_counter():
    with open("STORY.txt","r") as f:
        content = f.readlines()
        c = 0
        for i in content:
            if i[0] in ["I","M"]:
                c += 1

        print(c)
        print(content)


I_M_counter()
