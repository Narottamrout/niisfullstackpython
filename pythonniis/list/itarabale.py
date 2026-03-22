l=[78,45,78,23,90]
# l1=[i+2 for i in l]
# print(l1)
# l1=[i for i in l if i%2!=0]
# print(l1)
# l1=[i for i in l if i%2==0]
# print(l1)
#alter native code

i=0
while i<len(l):
	if l[i]%2!=0:
		l.remove(l[i])
	else:
		i+=1
print(l)			
		