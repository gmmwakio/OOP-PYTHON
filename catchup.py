class animals:
    def __init__(self,legs: int,eyes: int):
        self.legs = legs
        self.eyes = eyes

    def dog(self):
        print(f"I'm a dog with {self.legs} legs and {self.eyes} functional eyes.")

    def cat(self):
        print(f"I'm a Cog with {self.legs} legs and {self.eyes} functional eyes.")


class birds(animals):
    def __init__(self, legs, eyes,wingspan:float):
        super().__init__(legs, eyes)
        self.wingspan = wingspan

    def details(self):
        print(f"I'm a bird with {self.legs} legs, {self.eyes} and a wingspan of {self.wingspan} centimeters")
        
d1 = animals(4,2)
c1 = birds(2,2,171.2)
c2 = animals(4,3)

# d1.dog()
# c1.details()
# c2.cat()
d1.eyes ()
