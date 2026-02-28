def factest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=10
print("enter min range to maxrange")
min=int(input())
max=int(input())
s1=""
for i in range(min,max+1,1):
	s1=s1+str(i)+"!+"
	s=s+factest(i)
print("\b",s1,"=",s,sep="")
