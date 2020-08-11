def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

def knights(saying):
    def inner(qutoe):
        return "We are the knights who say: %s " %qutoe
    return inner(saying)