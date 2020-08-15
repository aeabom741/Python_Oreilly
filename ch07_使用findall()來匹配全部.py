import re
sourse = "Young Frankenstein"
n = re.findall('n',sourse)
if n:
    print('Find out')
print("Found ", len(n), ' matches')

n = re.findall('n.',sourse)
print(n)

n = re.findall('n.?',sourse)
print(n)