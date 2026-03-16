print("main start")
try:
	print(10//0)
except ZeroDivisionError:
	print("caught")
print("main end")