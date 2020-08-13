class car():
    def exclaim(self):
        print("I'am a car")
        
class yugo(car):
    def exclaim(self):
        print("I;m a Yugo!")
    def need_a_push(self):
        print("A little help here?")
        
give_me_a_car = car()
give_me_a_yugo = yugo()