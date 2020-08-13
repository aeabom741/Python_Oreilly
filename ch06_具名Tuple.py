from collections import namedtuple
Duck = namedtuple("Duck" , "bill tail")
duck = Duck("wide prange",'long')

Duck(bill = 'wide orange',tail = 'long')
print(duck.bill)
print(duck.tail)

parts = {'bill':'wide orange','tail':'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail = 'maganificien' , bill = 'crushing')
print(duck3)

duck_dict = {'bill':'wide orange','tail':'long'}
duck_dict['color'] = 'green'