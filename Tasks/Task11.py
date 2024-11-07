name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
gender = str(input("Enter your gender (Male or Female): "))
city = str(input("Enter your city (Metro or Non-metro): "))

if(age >= 25 and age <= 35 and gender == "Male" and city == "Metro"):
    print("Premium is 6%.")

elif(age >= 25 and age <= 40 and gender == "Male" and city == "Non-metro"):
    print("Premium is 4%.")

elif(age >= 25 and age <= 42 and gender == "Female" and city == "Metro"):
    print("Premium is 3%.")

elif(age >= 25 and age <= 45 and gender == "Female" and city == "Non-metro"):
    print("Premium is 2%.")

else:
    print("ERROR!!")