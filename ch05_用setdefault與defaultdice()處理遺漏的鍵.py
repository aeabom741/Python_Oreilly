from collections import defaultdict

prediodic_table = {'Hydrogen':1,'Helium':2}
print(prediodic_table)

prediodic_table.setdefault("Carbon",12)
print(prediodic_table)

prediodic_table_def = defaultdict(int)
prediodic_table_def['Hydrogen'] = 1
prediodic_table_def["Lead"]
print(prediodic_table_def)


def no_idea():
    return "Huh?"

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abc'
bestiary['b'] = 'def'
bestiary['c']
print(bestiary)
print('----------------------------------------------')

food_count = defaultdict(int)
for position in ['spam','spam','egg','spam']:
    food_count[position] += 1
for food ,count in food_count.items():
    print(food,count)
print('----------------------------------------------')

dict_count = {}
for food in ['spam','spam','egg','spam']:
    if not food in dict_count:
        dict_count[food] = 0
    dict_count[food] += 1

for food,count in dict_count.items():
    print(food,count)