
name=input("Enter UR name:")
words=name.split()
if(len(words)==0):
    print("Don't Enter Space for the name:")
else:
    res=True
    for word in words:
        if(   not word.isalpha()):

            res=False
            break
    if(res):
        print("{} is valid name".format(name))
    else:
        print("{} is invalid name".format(name))

