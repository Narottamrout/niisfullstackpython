#wap take a +ve number from keyboard cheak it is 2 digit number
n=int(input("enter a number"))
if n<0:
	n=-n
# if n>9:
# 	if n<100:
# 		print("it is two digit number")
if n>9 and n<100:
	print("2 digit number")
