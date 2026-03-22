l1=[[2,3,4],[5,7,8]]
l2=[[3,6,8],[9,7,6]]
l3=[[0,0,0],[0,0,0]]
for i in range(0,len(l1),1):
	for j in range(0,len(l1[i]),1):
		l3[i][j]=l1[i][j]+l2[i][j]
	print(l3)	