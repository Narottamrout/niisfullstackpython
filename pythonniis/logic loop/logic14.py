#count no of digit in the input number
# n=int(input("enter number"))
# count=0
# while n!=0:
# 	n=n//10
# 	count=count+1
# print("no of digit is",count)
'''write a program take a in put and display 
how many even or odd digit present in the number'''
n=int(input("enter number"))
ec=0
oc=0
while n!=0:
	r=n%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	n=n//10
print(oc)
print(ec)			
