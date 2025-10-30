class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return f"{self.brand} is driving"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Inheriting constructor
        self.model = model
    
    def honk(self):
        return f"{self.brand} {self.model} honks"

car = Car("Toyota", "Corolla")
print(car.drive())  # Toyota is driving (inherited method)
print(car.honk())   # Toyota Corolla honks (own method)

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
