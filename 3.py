import re
s = input()
x= re.search("[a-z]*_[a-z]*", s)
print(x)