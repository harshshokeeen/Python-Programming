#count the odd and even digits in number:-

n = int(input("Enter any number: "))
count = 0
count1 = 0
while(n > 0):
    if (n % 2 == 0):
        count = count + 1
        n = n//10
    elif (n % 2 != 0):
       count1 = count1 + 1
       n = n//10
print("Count of even numbers:", count)
print("Count of odd numbers:", count1)