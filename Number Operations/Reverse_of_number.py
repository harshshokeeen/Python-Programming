# print reverse of number:-

n = int(input("Enter any number: "))
#take initial reverse value 0.
reverse = 0

while(n > 0):
   #find the last digit 
    remainder = n % 10
   #append the last digit by shifting earlier num by 10 
    reverse = reverse * 10 + remainder
   #make the number smaller 
    n = n//10

print("Reversed number is:", reverse)