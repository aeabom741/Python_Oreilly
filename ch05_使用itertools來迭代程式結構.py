import itertools
for item in itertools.chain([1,2],['a','b']):
    print(item)
print('---------------------------------------')
for item in itertools.accumulate([1,2,3,4]):
    print(item)
