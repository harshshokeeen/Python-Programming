'''
Rectangle Class
•	Create a class called Rectangle with attributes:
        o	length: Length of the rectangle.
        o	width: Width of the rectangle.
•	Write methods to:
        o	Calculate and return the area of the rectangle.
        o	Calculate and return the perimeter of the rectangle.
•	Create instances of Rectangle, calculate their area and perimeter, and print the results.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(6, 3)  
rect2 = Rectangle(7, 5)  

print(f"Rectangle 1 (Length: {rect1.length}, Width: {rect1.width})")
print(f"Area: {rect1.area()}")          
print(f"Parimeter: {rect1.perimeter()}")

print("")

print(f"Rectangle 2 (Length: {rect2.length}, Width: {rect2.width})")
print(f"Area: {rect2.area()}")          
print(f"Parimeter: {rect2.perimeter()}")  