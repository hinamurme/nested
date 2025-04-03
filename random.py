while(True):
    sno=input("Enter Student Number(100-200):")
    if(sno.isdigit()):
        if(int(sno) in range(100,201)):
            break
        else:
            print("\t{} is Invalid Student Number".format(sno))
    else:
        if(sno.isspace() or len(sno)==0):
            print("\tDon't enter Space for Student Number-try again")
        elif(sno.isalnum()):
            print("\tDon't Alphabets / alnums for Student Number-try again")
        elif (not sno.isalnum()):
            print("\tDon't Symbols for Student Number-try again")
#Accept Student Name and Validate
while(True):
    sname=input("Enter Student Name:")
    words=sname.split()
    if(len(words)==0):
        print("\tDon't Enter Space for the Name:")
    else:
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            break
        else:
            print("\t{} is In Valid Name".format(sname))
#Accept Student Marks in C and Validate
while (True):
    cm = input("Enter Student Marks in C:")
    if (not cm.isdigit()):
        print("\tStudent Marks in C should not be non-integer-try again".format(cm))
    elif (int(cm) not in range(0, 101)):
        print("\t{} is Invalid Student Marks in C-try again".format(cm))
    else:
        break
#Accept Student Marks in CPP and Validate
while (True):
    cppm = input("Enter Student Marks in C++:")
    if (not cppm.isdigit()):
        print("\tStudent Marks in C++ should not be non-integer-try again".format(cppm))
    elif (int(cppm) not in range(0, 101)):
        print("\t{} is Invalid Student Marks in C++-try again".format(cppm))
    else:
        break
#Accept Student Marks in PYTHON and Validate
while (True):
    pym = input("Enter Student Marks in PYTHON:")
    if (not pym.isdigit()):
        print("\tStudent Marks in PYTHON should not be non-integer-try again".format(pym))
    elif (int(pym) not in range(0, 101)):
        print("\t{} is Invalid Student Marks in PYTHON-try again".format(pym))
    else:
        break
#Calculate totmarks
totmarks=int(cm)+int(cppm)+int(pym)
percent=round((totmarks/300)*100,2)
#Give the Grade
if(int(cm)<40 or int(cppm)<40 or int(pym)<40):
    grade="FAIL"
else:
    if(totmarks in range(250,301)):
        grade="DISTINCTION"
    elif(totmarks in range(200,250)):
        grade = "FIRST"
    elif (totmarks in range(150, 200)):
        grade = "SECOND"
    elif (totmarks in range(120, 150)):
        grade = "THIRD"
#Display Student Marks Report
print("*"*50)
print("\t\t\tSTUDENT MARKS REPORT")
print("*"*50)
print("\t\t\tStudent Number:{}".format(sno))
print("\t\t\tStudent Name:{}".format(sname))
print("\t\t\tStudent Marks in C:{}".format(cm))
print("\t\t\tStudent Marks in C++:{}".format(cppm))
print("\t\t\tStudent Marks in PYTHON:{}".format(pym))
print("\t\t\tStudent Total Marks:{}".format(totmarks))
print("\t\t\tStudent Percentage of Marks:{}".format(percent))
print("\t\t\tStudent Grade:{}".format(grade))
print("*"*50)






