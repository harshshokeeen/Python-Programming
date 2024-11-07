#Check whether the given number is power of 2 or not.

n = int(input("Enter any number: "))

def power_2(n):
    if (n <= 0):
        return False
    while (n % 2 == 0):
        n = n//2
    return n == 1

if power_2(n):
    print((n), "is the power of 2.")
else:
    print((n), "is NOT the power of 2.")