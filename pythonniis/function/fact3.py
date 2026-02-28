def factest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=factest(3)+factest(4)+factest(5)
print("3!+4!+5!=",s)	