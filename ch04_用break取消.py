while True:
    stuff = input("String to capitalize [type q to stop]:")
    if stuff == 'q':
        break
    else:
        print(stuff.capitalize())