class car():
    def exclaim(self):
        print("I'am a car")
        
class yugo(car):
    def exclaim(self):
        print("I'am a Yugo")
        
give_me_a_car = car()
give_me_a_yugo = yugo()

class person():
    def __init__(self,name):
        self.name = name
        
class MDPerson(person):
    def __init__(self,name):
        self.name = "Doctor " + name
        
class JDPerson(person):
    def __init__(self,name):
        self.name = name + ", Esquire"


person = person("Fudd")
doctor = MDPerson()