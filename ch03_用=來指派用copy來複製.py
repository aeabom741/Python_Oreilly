#參照
a = [1,2,3]
b = a
print(b)
a[0] = 8
print(b)
b[0] = "I'hate 8"
print(a)



a = ["Leo","Kelen","Wei"]
b = a.copy()
c = a[:]
d = list(a)