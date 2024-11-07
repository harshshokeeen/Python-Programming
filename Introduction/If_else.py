num = input("Enter any number: ")
print("Number is:", num)

if num % 2 == 0:
    print("Number is:", num)

dict = {
    "Name" : "Harsh",
    "Age" : 18,
    "Roll no." : 44
}

num = int(input("Enter any number: "))
if num % 2 == 1:
    print(dict["Name"])
else:
    print(dict["Roll no."])

print("Choose Head or Tail")
choice = input("Enter choice: ")

if (choice == "Head"):
    print("You WON!")
else:
    print("You LOSE!!")

#Ques not to do :- 5, 8
#Ques to must do :- 1 - 10 ( avoid 5 and 8 )