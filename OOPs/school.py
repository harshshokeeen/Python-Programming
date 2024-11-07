'''
School Class with Student Management
•	Create a class called School with attributes:
        o	school_name: Name of the school.
        o	students: A list to store students enrolled in the school.
•	Write methods to:
        o	Add a student to the list.
        o	Remove a student from the list by name.
        o	Display the names of all enrolled students.
•	Instantiate a School class, add students, remove one, and display the list of students.
'''

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
    
    def add_stu(self, student_name):
        self.students.append(student_name)
        print(f"'{student_name}' has been added to {self.school_name}.")
    
    def remove_stu(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"'{student_name}' has been removed from {self.school_name}.")
        else:
            print(f"'{student_name}' not found in the list of enrolled students.")
    
    def display_students(self):
        if self.students:
            print(f"List of students enrolled in {self.school_name} are:")
            for student in self.students:
                print(f"- {student}")
        else:
            print(f"No students are currently enrolled in {self.school_name}.")

school = School("S. R. Century Public School")

school.add_stu("Harsh")
school.add_stu("Ansh")
school.add_stu("Yuvraj")

school.display_students()

school.remove_stu("Ansh")

school.display_students()

school.remove_stu("Bhavesh")