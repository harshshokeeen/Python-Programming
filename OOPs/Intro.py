'''
Object- any entity that exists in real life.

Class- it is a blueprint that tells the structure of object.

Method- functions that are defined in class.
'''

'''
Difference between function and method:
user can make function irrespective of objects 
whereas methods are the functions that require 
funtion to operate and require class.
'''

'''
Class-
    Calculator          #Class
        add()           #Method
        sub()           #Method
    
        calculator object
        obj.add()           #Method

        print()             #Function (because it does not require any object)
'''

'''
class       #Function   #Keyword
Class Name  #class

example-            Human       #class
                    name
                    age

                    sleep()
                    eat()

Attribute: tells about data member
    name-
    dob-

def __init__(self, Uname, Udob):                      #Constructor(initialize) #self- to keep current record.

self.name = Uname                   #username
self.dob  = Udob                    #userDob

Constructor: it is a special type of function/method which initializez objects.
    Initialize- it allots space to object in memory. 
'''

'''
        CAR             #class
    brand
    year


Attributes:-
class Car:
    brand;
    year;

    def __init__(self, ibrand, iyear):
        self.brand = ibrand                 #setting value in attribute
        self.year  = iyear                  #setting value in attribute

    def display(self):
        print(self.brand)
        print(self.year)

#code will start from beginning.

car1 = car("AWM", 2010)                        #object- car1, class- car()
    car1.display()

car2 = car("BMW", 2025)
    car2.display()

'''