class Mydog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

pes = Mydog("Rex", 5, "Labrador")
print(pes.name)
print(pes.age)
print(pes.breed.upper())
print(pes.breed.lower())