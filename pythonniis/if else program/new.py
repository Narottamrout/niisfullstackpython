# n=int(input("enter number"))
# print("+ve") if n>0 else print("-ve")
sal=int(input("enter salary"))
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)