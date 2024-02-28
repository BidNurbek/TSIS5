import re
s = input()
x=re.sub("_[a-z]",lambda m:m.group()[-1].upper()  ,s)
print(x)