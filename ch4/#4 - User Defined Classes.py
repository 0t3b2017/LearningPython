## User-Defined Class - simple example
## Chapter 4 - Pg129 (181)

class Worker:
    def __init__(self, name, pay):          # Initialize when created
        self.name = name                    # self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]        # Split strings on blanks
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)            # Make two instances of the class Worker
sue = Worker('Sue Jones', 60000)            # Each has name and pay attrs

print(bob.lastName())                       # Call method: bob is self
print(sue.lastName())                       # Sue is the self subject

print(sue.pay)

sue.giveRaise(.10)                          # Updates sue's pay

print(sue.pay)