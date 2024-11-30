""" 
YOU DO - Create a vehicle class
"""

class Vehicle():
    def __init__(self, make, model, running=False):
        self.make = make
        self.model = model
        self.running = running

    def start(self):
        self.running = True
        print(f'Your {self.make} {self.model} has been turned on!')
    def stop(self):
        self.running = False
        print(f'Your {self.make} {self.model} has stopped!')

    # Overrides __init__ so when you directly print a dog object, it's something normal
    def __str__(self):
        return f"This is a vintage, state-of-the-art {self.make} {self.model}!"

car = Vehicle("Toyota", "RAV4")

print(car)
# prints: This is a vintage, state-of-the-art Toyota RAV4!

print(car.running) 
# prints: False

car.start()
# prints: Your Toyota RAV4 has been turned on!

print(car.running) 
# prints: True
