def  answer():
    print(42)
    
def run_function(func):
    func()
    
def add_args(arg1,arg2):
    print(arg1 + arg2)
    
def run_something_with_args(func,arg1,arg2):
    func(arg1,arg2)
    
def sum_arg(*arg):
    return sum(arg)

def run_with_positional_args(func,*args):
    return func(*args)
