#Write a Python program to reverse a 2-digit number.
num=int(input("enter the two digit number"))
FN=num//10
REM=num%10
rev=(REM*10)+FN
print("the reverse number is=",rev)
