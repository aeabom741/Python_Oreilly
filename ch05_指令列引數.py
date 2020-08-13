import sys
print('Program argument:',sys.argv)

def get_description():
    """Return random weather, just like pro"""
    from random import choice
    possibilities = ['rain','snow','sleet','fog','sun','who know']
    print(choice(possibilities))

get_description()