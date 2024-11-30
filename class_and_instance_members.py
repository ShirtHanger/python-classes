""" Class vs. instance members """

# Instance Attributes and Methods: 
# Linked to individual instances of a class. 
# Each object created from the class has its own copy of instance attributes. 
# For example, in a Dog class, each dog object has its own name and age attributes.

# Class Attributes and Methods:
# These belong to the class as a whole, not to any individual instance. 
# All instances of the class share the same class attributes. 
# If one instance changes a class attribute, that  change is reflected across all other instances. 
# These are intended to be accessed on the class only, not an instance 
# (although accessing them on the instance is technically possible).

""" 
To demonstrate class attributes, let’s add a next_id class attribute to the 
Dog class that can be used to assign an id to each dog instance:
"""

class Dog():
    # Adds an ID to each instance of a class, could be useful for APIs and databases
    next_id = 1

    def __init__(self, name, age=0):
        # Remember, this runs everytime a new dog object is created
        self.name = name
        self.age = age
        # assign current value of `next_id` to this instance
        self.id = Dog.next_id
        # increment the class attribute `next_id` so the next dog gets a new ID
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog #{self.id} named {self.name} is {self.age} years old.'
    
    # A class method 
    # Returns the number of dog objects by checking the next_id variable

    @classmethod
    def get_total_dogs(cls):
        # cls represents the Dog class, used similarly to self above
        amount_of_dogs = cls.next_id - 1
        return f'We have {amount_of_dogs} dogs... so far!'

harry = Dog('Harry', 2)
maggie = Dog('Maggie')
spot = Dog('Spot', 2)
diogee = Dog('Diogee')

print(harry)
#Dog #1 named Harry is 2 years old.

print(maggie)
#Dog #2 named Maggie is 0 years old.



# class methods are called on the class, not an instance
print(Dog.get_total_dogs()) 
# prints: 'We have {Number of Dogs} dogs... so far!'
# i.e: 'We have 4 dogs... so far!