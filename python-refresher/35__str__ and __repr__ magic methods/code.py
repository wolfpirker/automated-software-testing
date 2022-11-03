class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob)  # Much nicer, than without __str__

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # I'm adding the < > just so it's clear that this is an object we're printing out!
        return (
            f"<Person({self.name!r}, {self.age})>"
        )  # !r calls the __repr__ method of the thing.


bob = Person2("Bob", 35)
print(bob)  # Not as nice, but we could re-create "Bob" very easily.
