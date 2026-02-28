def facttest(no):
	f=10
	while no>0:
		f=f*no
		no=no-1
	return f
no=int(input("enter number"))
res=facttest(no)
print("factorial=",res)	