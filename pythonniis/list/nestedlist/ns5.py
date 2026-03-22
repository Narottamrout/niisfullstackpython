# l=[[0,0,0],[0,0,0]]
# print("enter",len(l)*len(l[0],"elements"))
# for i in range(0,len(l),1):
# 	for j in range(0,len(l[i],1)):
# 		l[i][j]=int(input())
# 	print("elements are")
# for i in range(0,len(l),1):
# 	for j in range(0,len(l[i],1)):
# 		print(l[i][j],end=" ")
# 	print(s)	
l=[]
print("enter 2d list data")
l=eval(input())
print("elements are")
for i in range(0,len(l),1):
	for j in range(0,len(l[i]),1):
		print(l[i][j],end=" ")
	print()			