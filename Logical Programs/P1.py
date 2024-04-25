#write a program to replace a chracter by another chracter
#in file "data.txt" where both chracters are given by user.

def Replace(old_char,new_char):
    file_obj = open("data.txt","r")
    content = file_obj.read()
    old_content = content
    new_content = content.replace(old_char,new_char)
    file_obj.close()

    file = open("data.txt","w")
    file.write(new_content)
    file.close()

    a = f"\n\"{old_char}\" is successfully replaced by \"{new_char}\""
    b = "Old Content:-",old_content
    c = "Updated Content:-",new_content

    return a,b,c

old_ch = input("Enter Chracter To Be Replaced:- ")
new_ch = input("Enter New Chracter:- ")

a,b,c = Replace(old_ch,new_ch)

print(a,"\n\n",b,"\n\n",c)

    
