##reverse a number
n=int(input("enter number"))
rev=0
while n!=0:
	rem=n%10
	rev=rev*10+rem
	n=n//10
print("the reverse no is ",rev)	


sum of the digit
sum=0
while n!=0:
	rem=n%10
	sum=sum+rem
	n=n//10
print(sum)	
