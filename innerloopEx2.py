i=1
while(i<=5):
    print("="*50)
    print("outer loop:value of i=",i)
    print("="*50)
    j=1
    while(j<=3):
        print("inner loop:value of j=",j)
        j=j+1
    else:
        print("________________________")
        print("\t Came out-off inner loop")
    i=i+1
else:
    print("="*50)
    print("come out-off outer loop")