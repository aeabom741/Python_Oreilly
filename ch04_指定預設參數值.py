def menu(wine,entree,dessert = 'pudding'):
    return {'wine':wine,"entree":entree,'dessert':dessert}

print(menu('chardonnary','chicken'))

def buggy(arg,result = []):
    result.append(arg)
    print(result)
    
def work(arg):
    result = []
    result.append(arg)
    return result

def bobuggy(arg,result = []):
    if result is None:
        result = []
    result.append(arg)
    print(result)