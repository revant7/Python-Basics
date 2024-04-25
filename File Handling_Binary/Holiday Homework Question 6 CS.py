def lower_case_counter():
    with open("STORY.txt","r") as f:
        content = f.read()
        c = 0
        for i in content:
            if i.islower():
                c += 1

        print(c)

lower_case_counter()
