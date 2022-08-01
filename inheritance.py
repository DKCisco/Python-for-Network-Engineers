class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sounds(self):
        return 'Woof'

class Frenchie(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def breathing(self):
        return "Gremlin"
    
    def sounds(self):
        return "YAP YAP"

murphy = Frenchie('Murphy', 1)
print(murphy.name)
print(murphy.age)
print(murphy.sounds())
print(murphy.breathing())

zeus = Dog('Zues', 2)
print(zeus.name)
print(zeus.age)
print(zeus.sounds())


