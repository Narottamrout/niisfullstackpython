def fact(n):
    if(n==1 or n==0):
        return 1
    fact=n*fact(n-1)
    return fact
n=int(input("enter number"))
print("the factorial is",fact(n))