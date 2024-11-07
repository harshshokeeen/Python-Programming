#(Ques10) Find out the grade , according to given percentage of the user.
#a.	>=90 print ‘A’ Grade
#b.	89 to 70 print ‘B’ Grade
#c.	69 to 50 print ‘C’ Grade
#d.	<50 print ‘D’ Grade

marks1 = float(input("Enter marks scored in 1st subject: "))
marks2 = float(input("Enter marks scored in 2nd subject: "))
marks3 = float(input("Enter marks scored in 3rd subject: "))
marks4 = float(input("Enter marks scored in 4th subject: "))
marks5 = float(input("Enter marks scored in 5th subject: "))

percentage = ((marks1+marks2+marks3+marks4+marks5)/500)*100
print("Percentage scored by student:", percentage)

if(percentage >= 90):
    if(percentage <= 100):
        print("Student scored 'A' grade.")

elif(percentage >= 70):
    if(percentage < 90):
        print("Student scored 'B' grade.")

elif(percentage >= 50):
    if(percentage < 70):
        print("Student scored 'C' grade.")

elif(percentage < 50 ):
    print("Student scored 'D' grade.")