import re
source = 'Young Frankenstein'
m = re.match("You",source)
if m:
    print(m.group())
    
m = re.match('^You',source)
if m:
    print(m.group())
print('------------------------')
m = re.match("Frank",source)
if m:
    print(m.groups())
    
m = re.search("Frank",source)
if m:
    print(m.group())
    
m = re.match('.*Frank',source)
if m:
    print(m.group())