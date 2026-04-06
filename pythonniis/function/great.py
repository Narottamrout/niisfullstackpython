def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greatest")
    elif(b>a and b>c):
        print("b is greatest")
    else:
        print("c is greatest") 
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
greatest(a,b,c)         