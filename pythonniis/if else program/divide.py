n=int(input("enter number"))
if n%5==0 and n%7==0:
	print("it is divisible by both 5 and 7")
elif n%5==0:
	print("it is divisible only 5")
elif n%7==0:
	print("it is divisible only 7")
else:
	print("it is invalid")		