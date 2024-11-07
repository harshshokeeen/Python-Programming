#(Ques6) Convert celsius into fahrenheit and vice versa.

celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius*9/5)+32

print("Entered temperature in Fahrenheit is", fahrenheit)

fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = (fahrenheit-32)*5/9

print("Entered temperature in celsius is", celsius)