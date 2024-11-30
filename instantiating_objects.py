class Dog():
    def __init__(self, name, age=0): 
        self.name = name
        self.age = age


    def bark(self): 
        print(f'{self.name} says woof!')


# Creating a new dog named Ruby, in a ruby variable
ruby = Dog('Ruby', 3)

print(ruby)
# prints some nonsense like: <__main__.Dog object at 0x7f24bc9d6ed0>

# print the `name` and `age` attributes of the ruby object
print(f'Name: {ruby.name}. Age: {ruby.age}')
# prints: Name: Ruby. Age: 3

# invoke the bark method for Ruby
ruby.bark()
# prints: Ruby says woof!

# don't pass a second argument for default age of 0
liam = Dog('Liam')

print(f'Name: {liam.name}. Age: {liam.age}')
# prints: Name: Liam. Age: 0
