l=[78,45,78,23,90]
l1=[]
i=0
for i in range(0,len(l),1):
	if i%2==0:
		l1.append(l[i])
	else:
		i=i+1
print(l1)			