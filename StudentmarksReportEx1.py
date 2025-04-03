while(True):
    sno= input("Enter Student Number(100,200):")
    if(sno.isdigit()):
        if(int(sno) in range(100,201)):
            break
    else:
        print("\t{} is Invalid Student Number".format(sno))
else:
    if(sno.isspace() or len(sno)==0):
     print("\tDon't Enter space for Student Number-try again")
    elif(sno.isalnum()):
            print("\tDon't Alphabets/alnums for Student Number-try again")
            #Accept Student Name and Validate
while(True):
    sname=input("Enter the Student Name:")
    words=sname.split()
    if(len(words)==0):
        print("\t Don't Enter Space for the Name:")
    else:
        res=True
        for word in  words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            break
        else:
          print("\t{} is invalid name".format(sname))
                #Accept Student Marks in c and Validate
while(True):
    cm=input("Enter Student Marks in C:")
    if(not cm.isdigit()):
         print("\tStudent Marks in C should not be non-integer-try again".format(cm))
    elif(int (cm) not in range(0,101)):
                print("\t{} is invalid Student Marks in C try again".format(cm))
    else:
        break
while(True):
   cppm=input("Enter Student Marks inC++:")
   if(not cppm.isdigit()):
            print("\t is invalid Marks in C++ try again".format(cppm))
   elif(int (cppm) not in range(0,101)):
         print("\t {} is invalid Student Marks in C++ try again".format(cppm))
   else:
    break
while(True):
    pym=input("Enter Student Marks in PYTHON:")
    if( not pym.isdigit()):
        print("\t  is invalid Student marks in PYTHON try  again".format(pym))
    elif(int (pym) not in range(0,101)):
        print("\t {}is Invalid Student marks in PYTHON try again".format(pym))
    else:
          break
totalmarks=int(cm)+int(cppm)+int(pym)
percent=round((totalmarks/300)*100,2)
#give the grade
if(int(cm)<40 or int(cppm)<40 or int(pym)<40):
        grade="FAIL"
else:
        if(totalmarks in range(250,301)):
            grade="DISTINCTION"
        elif(totalmarks in range(200,250)):
            grade="FIRST"
        elif(totalmarks in range(150,200)):
             grade="SECOND"
        elif(totalmarks in range(120,150)):
            grade="THIRD"
            #Display Student marks report
print("*" * 50)
print("\t\tSTUDENT MARKS REPORT")
print("*" * 50)
print("\t\tStudent number:{}".format(sno))
print("\t\tStudent name:{}".format(sname))
print("\t\tStudent Marks in C lang{}".format(cm))
print("\t\tStudent Marks in C++{}".format(cppm))
print("\t\tStudent Marks in Python{}".format(pym))
print("\t\ttotal marks{}".format(totalmarks))
print("\t\tStudent percentage of marks".format(percent))
print("\t\tStudent Grade:{}".format(grade))
print("*" * 50)












