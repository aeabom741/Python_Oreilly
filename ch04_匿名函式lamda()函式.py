def edit_story(words,func):
    for word in words:
        print(func(word))
        
def enlive(word):
    return word.capitalize() + "!"

stair = ['thud','meow','thud','hiss']

edit_story(stair,lambda word : word.capitalize())