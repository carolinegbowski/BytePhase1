

class Animal:

    def __init__(self, name, species, noise=""):
        self.name = name 
        self.species = species
        self.noise = noise
    
    def make_noise(self):
        print(self.noise)

class Tiger(Animal):

    def __init__(self, name):
        super().__init__(name, "tiger", "ROAR!")

    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog", "BARK!")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow", "MOO!")


class Zoo:
    
    def __init__(self):
        self.data = []
    def add(self, animal):
        self.data.append(animal)

    def show_animals(self):
        for animal in self.data: 
            print(f"{animal.name}, the {animal.species}")
            animal.make_noise()
     




    

        
        

