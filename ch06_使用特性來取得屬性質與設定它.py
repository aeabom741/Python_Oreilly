class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    def get_name (self):
        print("Inside Getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("Inside Setter")
        self.hidden_name = input_name
    name = property(get_name,set_name)
    
fowl = Duck("Howard")
print(fowl.name)
print(fowl.get_name())
print('------------------------')
fowl.name = 'Daffy'
print(fowl.name)
print('------------------------')
fowl.set_name("Daffy")
print(fowl.name)



class Suck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print("Inside getter")
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print("Inside setter")
        self.hidden_name = input_name
print('-----')
fow = Suck("Howard")
print(fow.name)
print('----')
fow.name = 'Dowland'
print(fow.name)
print('--------')
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
    
print(c.diameter())
    
c.radius = 7
c.diameter