class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def describe(self):
        print(f"This is {self.name}, a {self.species} who is {self.age} years old.")
    def celebrate_birthday(self):
        self.age = int(self.age) + 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old!")