# def show(a=0,b=0,c=0,d=0):
# 	print(a,b,c,d)
# show(10,20)
# show(7)
# show()
def show(a=0,*b):
 	print(a)
 	print(b)
show(10,20,30,40)
show("hi")
show()
show(1,7.5)	



