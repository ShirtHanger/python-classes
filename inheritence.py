from class_and_instance_members import *

""" 
Inheritance
We can create a subclass that inherits ALL the attributes/methods of the parent class (superclass)
It can also have a few of its own, unique attributes/methods
"""



# class Dog():
#     next_id = 1

#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#         self.id = Dog.next_id

#         Dog.next_id += 1

#     def bark(self):
#         print(f'{self.name} says woof!')

#     def __str__(self):
#         return f'Dog #{self.id} named {self.name} is {self.age} years old.'
    


#     @classmethod
#     def get_total_dogs(cls):

#         amount_of_dogs = cls.next_id - 1
#         return f'We have {amount_of_dogs} dogs... so far!'


# A subclass for dog!
class Circus_Dog(Dog):
    # add additional parameters AFTER those in the superclass
    def __init__(self, name, age=0, total_earnings=0):
        # always call the superclass's __init__ first
        Dog.__init__(self, name, age)
        # then add any new attributes
        self.total_earnings = total_earnings

    # add additional methods
    def add_prize_money(self, amount):
        self.total_earnings += amount
        print(f"{self.name}'s new total earnings are ${self.total_earnings}")
        
# let's make a new Circus_Dog!
        
winky = Circus_Dog('Winky', 3, 1000)

print(winky)
# prints: Dog #5 named Winky is 3 years old.

winky.bark()  
# prints: Winky says woof!
# the `Circus_Dog` class inherited the `Dog` class' `__str__()` and `bark()` method

print(winky.total_earnings)
# prints: 1000

winky.add_prize_money(500)
# prints: Winky's new total earnings are $1500
# a new method that instances of the 'Dog' class don't have

print(winky.total_earnings)
# prints: 1500
# go Winky go!
