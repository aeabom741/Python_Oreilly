number_list = []
for i in range(1,6):
    number_list.append(i)
print(number_list)
print('-------------------------')
number_list = list(range(1,6))
print(number_list)
print('-------------------------')
number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number -1 for number in range(1,6)]
print(number_list)
print('-------------------------')

odd_list = [number for number in range(1,9) if number % 2 == 1]
print(odd_list)

odd_list = []
for number in range(1,9):
    if number % 2 == 1:
        odd_list.append(number)
print(odd_list)

print('-------------------------')

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row,col)
        
        
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)