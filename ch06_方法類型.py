class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A")
    @classmethod
    def kids(cls):
        print("A has", cls.count , 'little objects')
        
easy_a = A()
breezy_a = A()
breezy_a.exclaim()
A.kids()

class coyotweapon():
    @staticmethod
    def commercial():
        print("This coyotweapon has been brought to you")
        
coyotweapon.commercial()