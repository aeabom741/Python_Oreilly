drinks = {
        'martini':{'vodka','vermouse'},
        'black russia':{'vodka','kahlua'},
        'white russia':{'cream','kahlua','vodka'},
        'manhattan':{'rye','vermouse','bitters'},
        'screwdriver':{'orange juice','vodka'}}

for name, content in drinks.items():
    if content & {'orange juice','vermouse'}:
        print(name)
print('-------------------------------------------------')
for name, content in drinks.items():
    if 'vodka' in content and not content &{'vermouse','cream'}:
        print(name)
print('-------------------------------------------------')
bruss = drinks['black russia']
wruss = drinks['white russia']

a = {1,2}
b = {2,3}
print("交集")
print(a & b)
print(a.intersection(b))
print(bruss & wruss)
print('-------------------------------------------------')
print("聯集")
print(a|b)
print(a.union(b))
print(bruss|wruss)
print('-------------------------------------------------')
print("差集")
print(a - b)
print(b - a)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)
print('-------------------------------------------------')
print("互斥或")
print(a^b) 
print(bruss ^ wruss)