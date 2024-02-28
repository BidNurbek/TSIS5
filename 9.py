import re
s = input()
x=re.sub("[A-Z]", lambda m:" "+m.group(), s)
print(x)