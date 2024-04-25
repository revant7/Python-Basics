def H_counter():
    with open("STORY.txt","r") as f:
        content = f.readlines()
        c = 0
        for i in content:
            if i[0] in ["H"]:
                c += 1

        print("The Number Of Lines Starting With H Are:",c)
        


H_counter()

