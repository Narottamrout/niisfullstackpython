a=int(input("enter number"))
b=int(input("enter number"))
print("enter choice")
ch=int(input())
match ch:
	case 1:print(a+b)
	case 2:print(a-b)
	case 3:print(a*b)
	# case_:print("invalid choice")