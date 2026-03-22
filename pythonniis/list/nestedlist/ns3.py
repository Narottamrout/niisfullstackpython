#display the element in matrix form using sequence
l=[[69,89,79],[23,67,89],[34,89,90]]
# for i in l:
# 	for j in i:
# 		print(j,end=" ")
# 	print()	 
#in anathor type
for i in range(0,len(l),1):
	for j in range(0,len(l[i]),1):
		print(l[i][j],end="\t")
	print()	
	