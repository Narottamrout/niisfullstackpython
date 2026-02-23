#convert upper case to lower case
# ch=input("enter character")
# ch=chr(ord(ch)+32)
# print(ch)
#anathor way to convert  upper case to lower case
print("enter a char")
ch=input()
if len(ch)>1:
	print("one character allow")
	sys.exit()
	if ch>='A' and ch<='Z':
		ch=chr(ord(ch)+32)
		print(ch)