class Human:
    _needs = ['air', 'water', 'food']
    def __init__(self, name):
        self._name = name
    
    @classmethod
    def needs(cls):
        return cls._needs

john = Human("john")

print(john._needs)

john._needs = ['pizza', 'ice cream', 'beer']

print(john._needs)

print(john.needs())

class Fashion:
    def __init__(self, style):
        self.style = style
    
    @classmethod
    def funky(cls):
        return cls(['bellbottoms', 'flowery shirt', 'big boots'])

    @classmethod
    def gothic(cls):
        return cls(['trench coat', 'leather jacket', 'doc martin boots'])

    @classmethod
    def casual(cls):
        return cls(['tshirt', 'jeans', 'sneakers'])

swimwear = Fashion(['trunks', 'towel'])

print(swimwear.style)

funky_fred = Fashion.funky()

print(funky_fred.style)

gothic_gary = Fashion.gothic()

print(gothic_gary.style)

casual_corey = Fashion.casual()

print(casual_corey.style)
