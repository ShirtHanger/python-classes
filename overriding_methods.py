class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    # Overrides __init__ so when you directly print a dog object, it's something normal
    def __str__(self):
        return f"My dog's name is {self.name}, and they are {self.age} years old."


ruby = Dog('Ruby', 3)

print(ruby)
# prints: My dog's name is Ruby, and they are 3 years old.
# No longer prints nonsense (<__main__.Dog object at 0x7f24bc9d6ed0>)

""" Sidenote - EVERYTHING in python is technically an object. Y
ou can see all of their attributes and methods with dir() """

# Like a list
nums = [1, 2, 3]

print(dir(nums))

""" Prints:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

print(dir(ruby))

""" Prints:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '
"""

# Overriding the __str__() method is an example of polymorphism. Having many forms!