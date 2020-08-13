class Qutoe():
    def __init__(self,person,word):
        self.person = person
        self.word = word
    def who(self):
        return self.person
    def says(self):
        return self.word + '.'
    
class QuestionQuote(Qutoe):
    def says(self):
        return self.word + '?'

class ExclamationQuote(Qutoe):
    def says(self):
        return self.word + '!'
    
hunter = Qutoe("Elmer Fudd","I'm hunting wabbits")
print(hunter.who(),hunter.says())

hunter1 = QuestionQuote("Bugs Banny","What's up doc")
print(hunter1.who(),'say:'+hunter1.says())

hunter2 = ExclamationQuote("Daffy Duck","It's a rabbit season")
print(hunter2.who(),'say:'+hunter2.says())