while True:
    value = input("Integer, Please [q to quit]:")
    if value == 'q':
        break
    number = int(value)
    if number == 2:
        continue
    else:
        print(number,"square is:",number*number)
        