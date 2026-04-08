#write a program initialize a number and reverse it
n=125
rev=0
while n!=0:
	rem=n%10
	rev=rev*10+rem
	n=n//10
print(rev)	
##palindrome number
n=int(input("enter number"))
temp=n
rev=0
while n!=0:
	rem=n%10
	rev=rev*10+rem
	n=n//10
if rev==temp:
		print("it is a palindrome no ")	
else:
	print("it is not a palindrome no")		