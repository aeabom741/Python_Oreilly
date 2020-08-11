def document_it(func):
    def new_function(*args,**kwargs):
        print("Function name:",func.__name__)
        print("Position argument:",args)
        print("Keyword argument:",kwargs)
        result = func(*args,**kwargs)
        print("Result:",result)
        return result
    return new_function



def square_it(func):
    def new_function(*args,**kwargs):
        result = func(*args,**kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_int(a,b):
    return a + b

add_int(5,6)