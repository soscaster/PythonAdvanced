from domains.course import Course
from domains.student import Student
from domains.mark import Mark
from input import input_student, input_courses, input_marks
from output import display_students, display_courses, display_marks, display_gpa
import os
# Remember to change cls to clear if you're using Mac or Linux
clear = lambda: os.system('clear')
import time

class Main:

    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def start(self):
        clear()

        # Input data for students
        self.students = input_student(self)
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        # Input data for courses
        self.courses = input_courses(self)
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        # Display data for students and courses
        display_students(self.students)
        display_courses(self.courses)
        # Press any key to continue
        input("Press any key to continue...")

        clear()
        # Input data for marks
        self.marks = input_marks(self.students, self.courses)
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        # Display data for marks
        display_marks(self.marks)
        input("Press any key to continue...")

        clear()
        # Display GPA of all students in descending order
        display_gpa(self.marks)
        input("Press any key to continue...")


if __name__ == "__main__":
    manage = Main()
    manage.start()
