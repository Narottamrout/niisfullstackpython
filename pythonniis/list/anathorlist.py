l=[78,45,67,23,44,90]
l1=[]
# for i in l:
# 	if i%2==0:
# 		l1.append(i)
# print(l1)	
for i in range(0,len(l),1):
	if l[i]%2==0:
		l1.append(l[i])
print(l1)			
