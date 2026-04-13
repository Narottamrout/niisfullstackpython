import re

pattern = re.compile(r'\d+')
result=pattern.findall('abc123def456')
print(result)