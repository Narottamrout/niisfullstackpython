# import re
# result=re.sub(r'\d+','x','abc123def456')
# print(result)
# import re
# result = re.search(r'\d+', 'dg3a457bc')
# print(result.group())\
import re
result=re.findall(r'\d','34gfh9h888f55jd')
print(result)
result = re.findall(r'\D+', 'a1b22c333')
print(result)