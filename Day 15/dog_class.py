# Day 15: basic class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Rex", "Labrador")
my_dog.bark()
print(f"{my_dog.name} is a {my_dog.breed}")