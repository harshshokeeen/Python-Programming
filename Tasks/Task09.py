#To give choice to user to perform arithmetic operations:

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print("1. For addition")
print("2. For subtraction")
print("3. For product")
print("4. For division")

choice = int(input())

if(choice == 1):
    print(num1 + num2)

elif(choice == 2):
    print(num1 - num2)

elif(choice == 3):
    print(num1 * num2)

elif(choice == 4):
    print(num1 / num2)

else:
    print("Invalid Choice!!")