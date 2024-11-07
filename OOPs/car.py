class Car:
    def __init__(self):
        self.brand = ""
        self.year = 0

    def setDetails(self):
        self.brand = input("Enter Brand: ") 
        self.year = int(input("Enter Year: ")) 

    def display(self):
        print(self.brand)
        print(self.year)

car1 = Car()
car1.setDetails()
car1.display()