# s1=eval(input("enter set data"))
# print(s1)
#take multiple data form keyboard
s=set()
print("how many data stored")
size=int(input())
for i in range(size):
	print("enter data",i+1)
	s.add(int(input()))
print(s)	