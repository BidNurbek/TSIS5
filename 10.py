import re
s = input()
x=re.sub("[A-Z]", lambda m:"_"+m.group().lower() , s)
print(x)