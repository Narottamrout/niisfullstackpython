#first way
# l=eval(input("enter list data"))
# # print(l)
#in second way
# l=[]
# s=int(input("how many data you want to enter in a list"))
# for i in range(0,s,1):
# 	print("enter element",i+1)
# 	l.append(int(input()))
# print(l)	
#third way to take input
l=[0,0,0,0,0]
for i in range(0,len(l),1):
	print("enter element",i+1)
	l[i]=int(input())
print(l)	
