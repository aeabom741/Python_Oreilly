import re
sourse = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''

wish = re.findall("wish",sourse)
print(wish)

fish = re.findall("wish|fish",sourse)
print(fish)

wish = re.findall("^I wish",sourse)
print(wish)

tonight = re.findall('fish tonight$',sourse)
print(tonight)

wf = re.findall('[wf]ish',sourse)
print('wf:',wf)

wsh = re.findall('[wsh]+',sourse)
print('wsh:',wsh)

ght = re.findall("ght\W",sourse)
print('ght:',ght)

I = re.findall("I (?=wish)",sourse)
print(I)

I = re.findall("(?<=I) wish",sourse)
print(I)