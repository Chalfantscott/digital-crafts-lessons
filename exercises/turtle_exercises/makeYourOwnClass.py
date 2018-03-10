class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Vehicle("Mazda", "6", "2004")

print car.make