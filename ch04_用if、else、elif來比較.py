disaster = True
if disaster:
    print("Woe")
else:
    print("Whee")
    
fury = True
small = True
if fury:
     if small:
         print("It's a cat")
     else:
         print("It's a bear")
else:
    if small:
        print("It's a stink")
    else:
        print("It's a human")
        
color = 'puce'
if color == 'red':
    print("It's a tomato")
elif color == 'green':
    print("It's a green pepper")
elif color == 'bee purple':
    print("I don't know what's that")
else:
    print("I've never hear of the color",color)

x = 7
5 < x and x < 10    

5 < x or x > 10

some_list = []
if some_list:
    print("There's something in here")
else:
    print("There's empty")