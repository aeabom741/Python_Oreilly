class Person():
    def __init__(self, name):
        self.name = name
        
class EmailPerson(Person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email = email
        
bob = EmailPerson("Bob" , "aeabom@gmail.com")

print(bob.name)
print(bob.email)