#check whether a number is palindrome or not:-

num = int(input("Enter a number: "))
num1 = num
rev = 0

while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num//10

print("Original number:", num)
print("Copied number:", num1)
print("Reversed number:", rev)

if (num1 == rev):
    print("The number is PALINDROME NUMBER.")
else:
    print("The number is NOT a PALINDROME NUMBER.")