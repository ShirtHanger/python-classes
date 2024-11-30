""" This is a dog class """

class Dog():
    #Initializing the class and its variables whenever a new Dog is created
    def __init__(self, name, age=0): 
        self.name = name
        self.age = age

    #A method
    def bark(self): 
        print(f'{self.name} says woof!')
