#(Ques4) Check whether the year is leap or not.

year = int(input("Enter any year: "))

if year % 4 == 0:
    print("The year you entered", year, "is a Leap year.")
elif year % 100 == 0:
    print("The year you entered", year, "is NOT a Leap year.")
elif year % 400 == 0:
    print("The year you entered", year, "is a Leap year.")
else:
    print("The year you entered", year, "is NOT a Leap year.")