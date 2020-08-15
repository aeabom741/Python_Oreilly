import re
sorce = 'Young Frankenstein'
m = re.search('Frank',sorce)
if m:
    print(m.group())