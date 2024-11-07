'''
Circle Class with Radius
•	Create a class called Circle with the following attributes:
        o	radius: Radius of the circle.
•	Write methods to:
        o	Calculate and return the area of the circle.
        o	Calculate and return the circumference of the circle.
•	Create instances of Circle, and print the area and circumference for each.
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * math.pi * self.radius

c1 = Circle(2)  
c2 = Circle(15)  

print(f"Circle 1 (Radius: {c1.radius})- ")
print(f"Area: {c1.area():.2f}")          
print(f"Circumference: {c1.circumference():.2f}")  

print("")

print(f"Circle 2 (Radius: {c2.radius})- ")
print(f"Area: {c2.area():.2f}")           
print(f"Circumference: {c2.circumference():.2f}")  