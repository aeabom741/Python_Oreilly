import re
sourse = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''

m = re.search(r'(. dish\b).*(\bfish)' , sourse)
print(m.group())

m = re.search(r"(?P<DISH>. dish\b).*(?P<FISH>\bfish)",sourse)
print(m.group())

print(m.group("FISH"))