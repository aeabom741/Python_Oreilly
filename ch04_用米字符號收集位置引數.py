def print_args(*args):
    print("Position argument tuple:", args)
    
print_args("3,2,1, wait")

def print_more(require1,require2,*args):
    print('Need this one:',require1)
    print('And need this one:',require2)
    print("All the rest:",args)
    