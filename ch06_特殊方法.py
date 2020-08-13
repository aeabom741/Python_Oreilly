class word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    
    
first = word("ha")
second = word("Ha")
third = word("eh")

print(first == second)

class word2():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word):
        return self.text.lower() == word.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word ("'+self.text +'")'
        
first = word2("ha")
print(first)