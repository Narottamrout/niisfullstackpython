def cal(no1,no2):
	return no1+no2,no1-no2,no1*no2,no1//no2
print ("enter two nos")
no1=int(input())
no2=int(input())
a,s,m,d=cal(no1,no2)
print(f"sum={a}\nsub={s}\nmult={m}\ndiv={d}")	