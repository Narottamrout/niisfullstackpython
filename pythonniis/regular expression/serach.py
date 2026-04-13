import re
result=re.search(r'\d+','abc123ab56c')
print(result.group())