'''
Person Class with Age Validation
•	Create a class named Person with attributes:
        o	name: Name of the person.
        o	age: Age of the person.
•	Write methods to:
        o	Display the person’s details.
        o	Ensure age is set to a positive number.
•	Try creating instances with different age values to see if the validation works.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = None  
        self.set_age(age)  

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Error: Age must be a positive number.")
            self.age = None  

    def display_details(self):
        if self.age is not None:
            print(f"Name: {self.name}, Age: {self.age}")
        else:
            print(f"Name: {self.name}, Age: Not available due to invalid age.")

p1 = Person("Harsh Shokeen", 18)  
p2 = Person("Ansh", -18)   
p3 = Person("Yuvraj", 0) 
p4 = Person("Bhavesh", 999)  

p1.display_details()
p2.display_details()
p3.display_details()
p4.display_details()