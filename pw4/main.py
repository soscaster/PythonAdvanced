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

    def input_student(self):
        clear()

        # Input data for students
        self.students = input_student(self)
        print("Please wait for 3 seconds...")
        time.sleep(3)
    

    def input_course(self):
        clear()
        # Input data for courses
        self.courses = input_courses(self)
        print("Please wait for 3 seconds...")
        time.sleep(3)

    def display_stu_cou(self):
        clear()
        # Display data for students and courses
        display_students(self.students)
        display_courses(self.courses)
        # Press any key to continue
        input("Press any key to continue...")

    def input_mark(self):
        clear()
        # Input data for marks
        self.marks = input_marks(self.students, self.courses)
        print("Please wait for 3 seconds...")
        time.sleep(3)

    def display_mark(self):
        clear()
        # Display data for marks
        display_marks(self.marks)
        input("Press any key to continue...")

    def stu_gpa(self):
        clear()
        # Display GPA of all students in descending order
        display_gpa(self.marks)
        input("Press any key to continue...")


if __name__ == "__main__":
    manage = Main()
    
    # Menu
    while True:
        clear()
        print("1. Input student(s) information")
        print("2. Input course(s) information")
        print("3. Display students and courses information")
        print("4. Input marks")
        print("5. Display marks of all students in all courses")
        print("6. Display and sort GPA of all students in descending order")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manage.input_student()
        elif choice == "2":
            manage.input_course()
        elif choice == "3":
            manage.display_stu_cou()
        elif choice == "4":
            manage.input_mark()
        elif choice == "5":
            manage.display_mark()
        elif choice == "6":
            manage.stu_gpa()
        elif choice == "7":
            break
        else:
            print("Invalid choice")