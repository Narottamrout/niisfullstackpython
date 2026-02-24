n = int(input("enter number: "))
n=-n
if n <= 9:
    print("single digit")
elif n > 9 and n < 100:
    print("no is double digit")
elif n >= 100 and n < 1000:
    print("no is triple digit")
else:
    print(" other number")