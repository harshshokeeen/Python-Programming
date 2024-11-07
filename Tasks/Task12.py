for i in range(1,11,1):
    print(i, "^", i, "=", i*i)

#Write a program to print power/square of a number if that
#number is divisible by 3.
#range is 1 to 30.

for i in range(1,31,1):
    if (i % 3 == 0):
        print(i, "^", i, "=", i*i)

#Write a program to:-
#print (Fizz) when a number is divisible by 7.
#print (Buzz) when a number is divisible by 5.
#print (fizzbuzz) when a number is divisible by 5 and 7.
#range is form 1 to 50.

for i in range(1,51,1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i, "FizzBuzz")
    elif (i % 7 == 0):
        print(i, "Fizz")
    elif (i % 5 == 0):
        print(i, "Buzz")