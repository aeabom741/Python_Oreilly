short_list = [1,2,3]
position = 5
try:
    print(short_list[position])
except:
    print("Need a position between 0 and ", len(short_list)-1, 'but got',position )
print('---------------------------------------------------------------------------')
while True:
    position = input("Enter position [q to stop]:")
    if position == 'q':
        break
    try:
        value = int(position)
        print(short_list[value])
    except IndexError as err:
        print("Bad index:",err)
    except Exception as other:
        print("Something else broke:",other)