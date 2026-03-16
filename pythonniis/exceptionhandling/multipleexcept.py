print("main start")
l=[10,30,50]
try:
	print(l[2]//0)
except IndexError as e:
	print("hi",e)
except ZeroDivisionError as d:
	print("bye",d)
except:
	print("handle all exception")
print("main end")				
