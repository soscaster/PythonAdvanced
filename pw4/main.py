from domains.course import Course
from domains.student import Student
from domains.mark import Mark
from input import input_student, input_courses, input_marks
from output import display_students, display_courses, display_marks
import os
# Remember to change cls to clear if you're using Mac or Linux
clear = lambda: os.system('cls')
import time


class Main:

    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def start(self):
        clear()
        self.students = input_student()
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        self.courses = input_courses()
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        display_students(self.students)
        display_courses(self.courses)
        
        # Press any key to continue
        input("Press any key to continue...")

        clear()
        self.marks = input_marks(self.students, self.courses)
        print("Please wait for 3 seconds...")
        time.sleep(3)

        clear()
        display_marks(self.marks)

if __name__ == "__main__":
    manage = Main()
    manage.start()
