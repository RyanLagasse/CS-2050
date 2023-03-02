class Animal:
    def __init__(self, name):
        self.name = name

    def reply(self):
        return self.speak()

class Mammal(Animal):
    def speak(self):
        return f"{self.name} says Hello!"

class Primate(Mammal):
    def speak(self):
        return f"{self.name} says Hola!"

class ComputerScientist(Primate):
    pass

class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"


'''
class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} is a {self.species}'

    #species as parameter
    def reply(self):
        return f'{self.name} says {"#fix"}'

class Mamal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.reply = f'{"#finish later"}'
        
class Cat(Mamal):
    def __init__(self, name):
        super().__init__(name)
        self.speak = f'{self.name} says meow!'

class Dog(Mamal):
    def __init__(self, name):
        super().__init__(name)
        self.speak = f'{self.name} says woof!'
        species = "Dog"

class Primate(Mamal):
    def __init__(self, name):
        super().__init__(name)
        self.speak = f'{self.name} says hola!'

class Computer_Scientist(Primate):
    def __init__(self, name):
        super().__init__(name)

#testing code with prints
#only worked on dog class others are just there

Bud = Dog("bud")
Messi = Computer_Scientist("Magic Messi")
print(Messi.name)
print(Messi.speak)

'''