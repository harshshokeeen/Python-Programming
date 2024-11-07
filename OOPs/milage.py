'''
Car Class with Mileage
•	Create a Car class with attributes:
        o	make: The make of the car.
        o	model: The model of the car.
        o	year: The year of manufacture.
        o	mileage: The current mileage of the car.
•	Write methods to:
        o	Display car details.
        o	Update the mileage.
        o	Check if the car qualifies as an “old” car (older than 10 years).
•	Create instances of the Car class and test these methods.
'''

from datetime import datetime

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_details(self):
        print(f"Details about car: ")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")
    
    def update_mileage(self, new_mileage):
        if new_mileage > self.mileage:
            self.mileage = new_mileage
            print(f"Mileage of the car is updated to {self.mileage} miles.")
        else:
            print("New mileage must be greater than the current mileage.")
    
    def is_old(self):
        current_year = datetime.now().year
        car_age = current_year - self.year
        if (car_age > 10):
            return True
        else:
            return False

car1 = Car("Toyota", "Fortunar", 2012, 120000)
car2 = Car("BMW", "M8 Compition", 2024, 50000)

print("Details of car1: ")
car1.display_details()
print(f"Is Car 1 old? {'Yes' if car1.is_old() else 'No'}\n")

print("Details of car2: ")
car2.display_details()
print(f"Is Car 2 old? {'Yes' if car2.is_old() else 'No'}\n")

car1.update_mileage(125000)

print(f"Is Car 1 old after mileage update? {'Yes' if car1.is_old() else 'No'}")