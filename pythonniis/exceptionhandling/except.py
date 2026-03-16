print("main start")
try:
	print(10//0)
except BaseException:
	print("caught")
print("main end")	