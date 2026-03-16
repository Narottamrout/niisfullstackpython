l=[90,67,45]
try:
	res=l[2]//0
except:
	print("handle all exception")
else:
	print("else block",res)
print("main end")			