import sys
sys.dont_write_bytecode = True
from domains.course import Course
from domains.student import Student
from domains.mark import Mark
from input import input_student, input_courses, input_marks, load_students, load_courses, load_marks
from output import display_students, display_courses, display_marks, display_gpa
import zipfile
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

        # Check if students.dat exists
        if os.path.exists("students_pkl.dat"):
            clear()
            print("Detected students_pkl.dat file!")
            print("-----------------")
            # Decompress and load data from it
            print("Decompressing files...")
            with open("students_pkl.dat", "rb") as infile:
                with zipfile.ZipFile(infile, "r") as zipf:
                    zipf.extractall()
                    # Load data from extracted files
                    self.courses = load_courses()
                    self.students = load_students()
                    self.marks = load_marks(self.students, self.courses)
            print("Decompress files successfully!")
            print("-----------------")
            print("Please wait for 3 seconds...")
            time.sleep(3)

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

    def compress_pkl_files(self):

        # Compress all files txt into students.dat
        print("Compressing pkl files to students_pkl.dat ...")
        with open("students_pkl.dat", "wb") as outfile:
            with zipfile.ZipFile(outfile, "w") as zipf:
                for file in os.listdir():
                    if file.endswith(".pkl"):
                        zipf.write(file)
        print("Compress files successfully!")
        print("-----------------")

        # Delete the previous students.pkl file
        print("Deleting previous pickle files...")
        if os.path.exists("students.pkl"):
            os.remove("students.pkl")
        # Delete the previous courses.pkl file
        if os.path.exists("courses.pkl"):
            os.remove("courses.pkl")
        # Delete the previous marks.pkl file
        if os.path.exists("marks.pkl"):
            os.remove("marks.pkl")
        print("Delete files successfully!")
        print("-----------------")

if __name__ == "__main__":
    manage = Main()

    # Menu
    while True:
        clear()
        print("Student Management System")
        print("1. Input student(s) information")
        print("2. Input course(s) information")
        print("3. Display students and courses information")
        print("4. Input marks")
        print("5. Display marks of all students in all courses")
        print("6. Display and sort GPA of all students in descending order")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # If the user already input the student information, ask them if they want to override it
            if len(manage.students) > 0:
                print("-----------------")
                print("You have already input the student information")
                print("Do you want to override it?")
                print("1. Yes")
                print("2. No")
                choice = input("Enter your choice: ")
                if choice == "1":
                    manage.input_student()
                elif choice == "2":
                    pass
                else:
                    print("Invalid choice")
            else:
                manage.input_student()   
        elif choice == "2":
            # If the user already input the course information, ask them if they want to override it
            if len(manage.courses) > 0:
                print("-----------------")
                print("You have already input the course information")
                print("Do you want to override it?")
                print("1. Yes")
                print("2. No")
                choice = input("Enter your choice: ")
                if choice == "1":
                    manage.input_course()
                elif choice == "2":
                    pass
                else:
                    print("Invalid choice")
            else:
                manage.input_course()
        elif choice == "3":
            manage.display_stu_cou()
        elif choice == "4":
            # If the user already input the mark information, ask them if they want to override it
            if len(manage.marks) > 0:
                print("-----------------")
                print("You have already input the mark information")
                print("Do you want to override it?")
                print("1. Yes")
                print("2. No")
                choice = input("Enter your choice: ")
                if choice == "1":
                    manage.input_mark()
                elif choice == "2":
                    pass
                else:
                    print("Invalid choice")
            else:
                manage.input_mark()
        elif choice == "5":
            manage.display_mark()
        elif choice == "6":
            manage.stu_gpa()
        elif choice == "7":
            clear()
            manage.compress_pkl_files()
            print("Thank you for using my program!")
            break
        else:
            print("Invalid choice")