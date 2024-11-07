'''
Employee Class
•	Create an Employee class with the following attributes:
        o	name: Employee name.
        o	salary: Salary of the employee.
•	Write methods to:
        o	Display employee information.
        o	Give a raise by a certain percentage.
•	Create multiple employees, give them raises, and display their updated details.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Name of the employee: {self.name}")
        print(f"Salary of the employee: ${self.salary:.2f}")
    
    def give_raise(self, percentage):
        if percentage > 0:
            raise_amount = (self.salary * percentage) / 100
            self.salary += raise_amount
            print(f"Salary of the employee is raised by {percentage}%. Updated salary of the employee: ${self.salary:.2f}")
        else:
            print("Raise percentage must be positive.")

employee1 = Employee("Ansh", 500000)
employee2 = Employee("Harsh", 600000)
employee3 = Employee("Yuvraj", 550000)

print("Initial Employee Details: ")
employee1.display_info()
employee2.display_info()
employee3.display_info()

employee1.give_raise(11)  
employee2.give_raise(13)   
employee3.give_raise(9)   

print("\nUpdated Employee Details: ")
employee1.display_info()
employee2.display_info()
employee3.display_info()