class Mamal:
    def __init__(self):
        pass
    
    def features(self):
        print('It has fur and mammary glands')

class Dog(Mamal):
    def __init__(self):
        pass
    
    def bark(self):
        print('Woof!!')
    
    def walking(self):
        print('Happily strolling')
        
    def eat(self):
        print('Happily eating')

class Puppy(Dog):
    def __init__(self):
        pass

    def play(self):
        print('Paying and biting shoes')
        
puppy1 = Puppy()
puppy1.bark()
puppy1.play()
puppy1.features()