place ='caf\u00e9'
place_byte = place.encode('utf-8')
print(place_byte)
print(type(place_byte))

place2 = place_byte.decode('utf-8')
print(place2)

place4 = place_byte.decode("latin-1")
print(place4)

place5 = place_byte.decode('windows-1252')
print(place5)