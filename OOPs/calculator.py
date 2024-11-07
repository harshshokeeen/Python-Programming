'''
Calculator Class
•	Create a class named Calculator with methods to perform basic arithmetic operations:
        o	add(a, b): Adds two numbers.
        o	subtract(a, b): Subtracts one number from another.
        o	multiply(a, b): Multiplies two numbers.
        o	divide(a, b): Divides one number by another, with a check to prevent division by zero.
•	Instantiate the Calculator class and perform all operations.
'''

class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            return "Error!!, division BY ZERO is not possible."
        else:
            return a / b
        
cal = Calculator()

a, b = 10, 5
add_res = cal.add(a, b)
print(f"{a} + {b} = {add_res}")

sub_res = cal.sub(a, b)
print(f"{a} - {b} = {sub_res}")

multi_res = cal.multi(a, b)
print(f"{a} * {b} = {multi_res}")

div_res = cal.div(a, b)
print(f"{a} / {b} = {div_res}")

zero_div_res = cal.div(a, 0)
print(f"{a} / 0 = {zero_div_res}")