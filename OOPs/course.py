'''
Course Enrollment System
•	Create a Course class with attributes:
        o	course_name: Name of the course.
        o	students: A list of enrolled students.
•	Write methods to:
        o	Enroll a student.
        o	Remove a student.
        o	Display the list of students enrolled in the course.
•	Create instances of the Course class, enroll students, and display the list.
'''

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_stu(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} has been enrolled in {self.course_name}.")
        else:
            print(f"{student_name} is already enrolled in {self.course_name}.")

    def remove_stu(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from {self.course_name}.")
        else:
            print(f"{student_name} is not enrolled in {self.course_name}.")

    def display_enrolled_stu(self):
        if self.students:
            print(f"\nStudents enrolled in {self.course_name} are:")
            for student in self.students:
                print(student)
        else:
            print(f"No student enrolled in {self.course_name}.")


python_course = Course("~Introduction to Python~")

python_course.enroll_stu("Ansh")
python_course.enroll_stu("Harsh")
python_course.enroll_stu("Yuvraj")
python_course.enroll_stu("Ansh")  

python_course.display_enrolled_stu()

python_course.remove_stu("Yuvraj")

python_course.display_enrolled_stu()

python_course.remove_stu("Bhavesh")

python_course.display_enrolled_stu()