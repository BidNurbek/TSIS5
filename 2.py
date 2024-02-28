import re
s=input()
x=re.fullmatch("ab{2,3}", s)
print(x)