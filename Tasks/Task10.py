#Write a program to:-
#print square of number if it is EVEN
#print number x 2 if it is odd
#range is 1 to 20

for i in range(1,20,1):
    if (i % 2 == 0):
        print(i, i, "*", i, "=", i*i)
    elif (i % 2 != 0):
        print(i, i, "*", 2, "=", i*2)