def do_nothing():
    pass

def make_a_sound():
    print("quack")
make_a_sound()

def agree():
    return True

if agree():
    print("Splendid")
else:
    print("That was unexpected")
    
def echo(anything):
    return anything + ' ' + anything

echo("sadasdf")

def commentry(color):
    if color == 'red':
        return "It's a tomato"
    elif color == 'green':
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color",color
    
commen = commentry("blue")
print(commen)