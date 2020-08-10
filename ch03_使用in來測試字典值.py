drinks = {
        'martini':{'vodka','vermouse'},
        'black russia':{'vodka','kahlua'},
        'white russia':{'cream','kahlua','vodka'},
        'manhattan':{'rye','vermouse','bitters'},
        'screwdriver':{'orange juice','vodka'}}

for name, content in drinks.items():
    if 'vodka' in content:
        print(name)
        
print('-------------------------------------------------')
for name, content in drinks.items():
    if 'vodka' in content and not('vermouse' in content or 'cream' in content):
        print(name)