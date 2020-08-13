quote = {
        'Moe':'A wise guy , huh?',
        'Larry':'ow!',
        'Curly':'Nyuk Nyuk!',}
for stoog in quote:
    print(stoog)
print('---------------------------------')
    
from collections import OrderedDict
quote = OrderedDict([
        ('Moe','A wise guy , huh?'),
        ('Larry','ow!'),
        ('Curly','Nyuk Nyuk!'),
        ])
    
for stoog in quote:
    print(stoog)