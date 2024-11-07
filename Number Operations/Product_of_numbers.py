#product of n natural numbers:-

n = int(input("Enter any natural number: "))

product = 1

for i in range(1,n+1):
    product = product * i

print("Product of the number is:", product)