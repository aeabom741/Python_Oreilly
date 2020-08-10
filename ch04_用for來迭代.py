rabbits = ["Flopsy",'Mospy','Cottontail','peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
print('------------------------------------------')
for rabbit in rabbits:
    print(rabbit)
print('------------------------------------------')
word = 'cat'
for letter in word:
    print(letter)
print('------------------------------------------')
accusation = {'room':'ballroom','weapon':'lead pipe','person':'col'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)
    
for item in accusation.items():
    print(item)
    
for card, content in accusation.items():
    print('Card',card,'has the content:'+content)