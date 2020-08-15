import string
import re
printable = string.printable
print(len(printable))
print(printable[:50])

#找數字
number = re.findall('\d',printable)
print(number)

#找文字
word = re.findall('\w',printable)
print(word)

#找空白
space = re.findall('\s',printable)
print(space)

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w',x))