l=[90,45,34]
try:
	print(l[1]//0)
except Exception as e:
	print("print",e)
finally:
	print("must execute")
print("end")