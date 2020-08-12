animal = 'fruitbat'
def print_global():
    print("inside print_global:"+animal)
    
print("at the top level:"+animal)
print_global()

print('--------------------------------------')
def change_local():
    animal =  'wobat'
    print('inside change_local:', animal)

change_local()
print(animal)

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wobat'
    print("inside change_and_print_global animal:" + animal)
    
change_and_print_global()
print(animal)