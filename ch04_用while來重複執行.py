count = 1
while count < 5:
    print(count)
    count += 1
    
    
while True:
    stuff = input("String to capitalize [type q to stop]")
    if stuff == 'q':
        break
    else:
        print(stuff.capitalize())