s={7,8,3,5}
ele=8
rep=0
for i in s:
	if i==ele:
		s.remove(ele)
		s.add(rep)
print(s)		