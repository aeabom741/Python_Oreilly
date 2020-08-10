python = {
        'Chapman':'Graham',
        'Cleese':'Jhon',
        'Idle':'Eric',
        'Palin':'Micheal'}

python["Gilliam"] = 'Gerry'
print(python)

python["Gilliam"] = 'Terry'
print(python)

python["Gilliam"] = 'Jones'
print(python)

other = {"Marx":"Groucho","Howard":'Moe'}
python.update(other)

first = {"a":1,"b":2}
second = {"b":'platypus'}
first.update(second)
