#(Ques3) WAP to swap two numbers with and without using third variable.

##With third variable-

print("Before swaping: ")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("After swapping: ")

num3 = num1
num1 = num2 
num2 = num3 

print("1st number:", num1)
print("2nd number:", num2)

##without third variable-                              

print("Before swaping: ")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("After swapping: ")

num1, num2 = num2, num1

print("1st number:", num1)
print("2nd number:", num2)