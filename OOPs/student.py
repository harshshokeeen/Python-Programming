'''
class = student
attributes = name, age, grade
member functions = display and greet student

Task- You have to greet them and display their information.
'''

class student:
    def display_greet(self):
        print("Hello", self.name, "greetings.")
        print("Name of the student: ", self.name)
        print("Age of the student: ", self.age)
        print("Grade of the student: ", self.grade)
        print("===============================")

    def __init__(self, uname, uage, ugrade):
        self.name = uname
        self.age = uage
        self.grade = ugrade

stu1 = student("Ram", 18, 'E')
stu1.display_greet()

stu2 = student("Harsh", 18, 'E')
stu2.display_greet()

stu3 = student("Bhavesh", 18, 'A')
stu3.display_greet()

stu4 = student("Ansh", 18, 'B')
stu4.display_greet()

stu5 = student("Yuvraj", 18, 'C')
stu5.display_greet()

stu6 = student("Himanshu", 18, 'D')
stu6.display_greet()