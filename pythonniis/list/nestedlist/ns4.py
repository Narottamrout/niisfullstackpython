#using input we can write a list
# l=[]
# s=int(input("how many list store in the list"))
# for i in range(0,s,1):
# 	x=[]
# 	print("enter list data")
# 	x=eval(input())
# 	l.append(x)
# print("elements are")
# for i in range(0,len(l),1):
# 	for j in range(0,len(l[i]),1):
# 		print(l[i][j],end=" ")
# 	print()	
# l=[]
# s=int(input("enter how many list store"))
# for i in range(0,s,1):
# 	x=[]
# 	print("enter list data")
# 	x=eval(input())
# 	l.append(x)
# print("elements are")
# for i in range(0,len(l),1):
# 	for j in range(0,len(l[i]),1):
# 		print(l[i][j],end=" ")
# 	print()	
#anathor way
print("how many list store")
s=int(input())
for i in range(0,s,1):
	x=[]
	print("enter list",i+1,"how many data")
	s1=int(input())
	for j in range(0,s1,1):
		print("enter element",j+1)
		x.append(int(input()))
		l.append(x)
print("elements are")
for i in range(0,len(l),1):
	for j in range(0,len(l[i],1)):
		print(l[i][j],end=" ")
	print()				