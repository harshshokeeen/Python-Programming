#print sum of all digits of number:

num = int(input("Enter any number: "))

sum = 0

while(num > 0):
    remainder = num % 10
    sum = sum + remainder
    num = num//10
print("Sum of the digits is:", sum)