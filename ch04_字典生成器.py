word = 'letters'
letter_count = {a: word.count(a) for a in word}
print(letter_count)

word = 'letters'
letter_count = {letter: word.count(letter) for letter in set(word)}
print(letter_count)

