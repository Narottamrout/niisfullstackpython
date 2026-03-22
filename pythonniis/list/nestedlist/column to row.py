#display row column to column row
# l1=[[1,2,3],[4,5,6]]
# l2=[[0,0],[0,0],[0,0]]
# for i in range(0,len(l1),1):
# 	for j in range(0,len(l1[i]),1):
# 		l2[j][i]=l1[i][j]
# 	print(l2)	
#without using list compression
# l1=[[1,2,3],[4,5,6]]
# l2=[]
# for i in l1:
# 	x=[]
# 	for j in i:
# 		x.append(j)
# 		l2.append(x)
# 	print(l2)	
#using list compression
# l1=[[1,2,3],[4,5,6]]
# l2=[[j for j in i] for i in l1]
# print(l2)