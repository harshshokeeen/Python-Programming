for i in range(10):
    print(i)

#Iteration: repetation (here it's done 10 times)
#Always starts with 0
#Will end with (range value -1)

for i in range(5):
    print(i,". Hello")

#Behind the scene:-
#range(5): range is (0, 5, 1).
#0 is the starting value.
#By default it always starts with 0.
#5 is the ending value.
#Interation will be there 5 times.
#1 is the increment value.

for i in range(0,10,2):
    print(i)

for i in range(3,20,4):
    print(i)

for i in range(0,-5,-1):     #To go in negative values.
    print(i)