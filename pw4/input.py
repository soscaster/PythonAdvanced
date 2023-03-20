from domains.course import Course
from domains.student import Student
import time
import os
clear = lambda: os.system('clear')

def input_student(self):
    print("----- WELCOME -----")
    # Input the number of students are going to be input
    stunum = int(input("Number of students you want to import: "))

    # If stunum is less than 0, then the program will ask you to input again
    if stunum < 0:
        print("---------------------------")
        print("Please input positive number only!")
        print("---------------------------")
        print("Please wait for 1 second...")
        time.sleep(2)
        # os.system("cls")
        clear()
        self.input_students()

    students = {}
    print("-----------------")
    i = 0
    # Loop through and get input for each student
    for i in range(stunum):
        i = i + 1
        print(f"\nLet's input information for Student No. {i}")
        stu_id = input("Student ID: ")
        stu_name = input("Student name: ")
        stu_dob = input("Student DOB: ")
        # Create a new student object
        student = Student(stu_id, stu_name, stu_dob)
        # Add the student object to the dictionary
        students[stu_id] = student
        print("Student No.", i, " information has been imported successfully!")
        print("--------------------------------------------")
    return students

def input_courses(self):
    # Input the number of courses to import
    cou_num = int(input("Number of courses you want to import: "))
        
    # If cou_num is less than 0, then the program will ask you to input again
    if cou_num < 0:
        print("---------------------------")
        print("Please input positive number only!")
        print("---------------------------")
        print("Please wait for 1 second...")
        time.sleep(2)
        # os.system("cls")
        clear()
        self.input_courses()

    courses = {}
    i = 0
    # Loop through and get input for each course
    for i in range(cou_num):
        i = i + 1
        print(f"\nLet's input information for Course No. {i}")
        cou_id = input("Course ID: ")
        cou_name = input("Course name: ")
        cou_credit = int(input("Course credit(s): "))
        # Create a new course object
        course = Course(cou_id, cou_name, cou_credit)
        # Add the course object to the dictionary
        courses[cou_id] = course
        print("Course No.", i, " information has been imported successfully!")
        print("--------------------------------------------")
    return courses

def input_marks(students, courses):
    marks = {}
    for cou_id in courses:
        # Ask for the marks of the students for each course
        print(f"Please input marks for course ID {cou_id}:")
        for stu_id in students:
            mark = float(input(f"Student {students[stu_id].id}'s mark: "))
            # Create a new mark object
            new_mark = {
                "student": students[stu_id],
                "course": courses[cou_id],
                "mark": mark
            }
            # Add the mark object to the dictionary
            marks[(stu_id, cou_id)] = new_mark
        print("-----------------")
    return marks
