from domains.course import Course
from domains.student import Student
from domains.mark import Mark
import threading
import pickle
import time
import os
clear = lambda: os.system('clear')

class SavePickleThread(threading.Thread):
    def __init__(self, pickle_data, filename):
        threading.Thread.__init__(self)
        self.pickle_data = pickle_data
        self.filename = filename

    def run(self):
        with open(self.filename, "wb") as p:
            pickle.dump(self.pickle_data, p)

def load_courses():
    if os.path.exists("courses.pkl"):
        courses = pickle.load(open("courses.pkl", "rb"))
    else:
        print("File 'courses.pkl' does not exist!")
        courses = {}
    return courses

def load_students():
    if os.path.exists("students.pkl"):
        students = pickle.load(open("students.pkl", "rb"))
    else:
        print("File 'students.pkl' does not exist!")
        students = {}
    return students

def load_marks(students, courses):
    if os.path.exists("marks.pkl"):
        marks = pickle.load(open("marks.pkl", "rb"))
    else:
        print("File 'marks.pkl' does not exist!")
        marks = {}
    return marks

def input_student(self):
    print("----- WELCOME -----")
    try:
        # Input the number of students are going to be input
        stunum = int(input("Number of students you want to import: "))
        if stunum < 0:
            clear()
            print("---------------------------")
            print("Please input positive number only!")
            print("---------------------------")
            print("Please wait for 1 second...")
            time.sleep(2)
            # os.system("cls")
            clear()
            self.input_student()
    except ValueError:
        clear()
        print("---------------------------")
        print("Please input positive number only!")
        print("---------------------------")
        print("Please wait for 1 second...")
        time.sleep(2)
        # os.system("cls")
        clear()
        self.input_student()
    
    students = {}
    print("-----------------")
    i = 0
    # Loop through and get input for each student
    for i in range(stunum):
        i = i + 1
        print(f"Let's input information for Student No. {i}")
        stu_id = input("Student ID: ")
        stu_name = input("Student name: ")
        stu_dob = input("Student DOB: ")
        # Create a new student object
        student = Student(stu_id, stu_name, stu_dob)
        # Add the student object to the dictionary
        students[stu_id] = student
        print("Student No.", i, " information has been imported successfully!")
        print("--------------------------------------------")

        # Write the student information to the file
        SavePickleThread(students, "students.pkl").start()
    if len(students) != 0:
        print("Database of student has been imported!")
        return students
    else:
        print("Check the code!")
        return students
    

def input_courses(self):
    try:
        # Input the number of courses to import
        cou_num = int(input("Number of courses you want to import: "))
    except ValueError:
        print("---------------------------")
        print("Please input positive number only!")
        print("---------------------------")
        print("Please wait for 1 second...")
        time.sleep(2)
        # os.system("cls")
        clear()
        input_courses()
    # If cou_num is less than 0, then the program will ask you to input again
    if cou_num < 0:
        print("---------------------------")
        print("Please input positive number only!")
        print("---------------------------")
        print("Please wait for 1 second...")
        time.sleep(2)
        # os.system("cls")
        clear()
        input_courses()

    courses = {}
    print("-----------------")
    i = 0
    # Loop through and get input for each course
    for i in range(cou_num):
        i = i + 1
        print(f"Let's input information for Course No. {i}")
        cou_id = input("Course ID: ")
        cou_name = input("Course name: ")
        cou_credit = int(input("Course credit(s): "))
        # Create a new course object
        course = Course(cou_id, cou_name, cou_credit)
        # Add the course object to the dictionary
        courses[cou_id] = course
        print("Course No.", i, " information has been imported successfully!")
        print("--------------------------------------------")

        # Write the course information to the file
        SavePickleThread(courses, "courses.pkl").start()

    if len(courses) != 0:
        print("Database of course has been imported!")
        return courses
    else:
        print("Check the code!")
        return courses

def input_marks(students, courses):
    marks = {}
    for cou_id in courses:
        # Ask for the marks of the students for each course
        print(f"Please input marks for course ID {cou_id}:")
        for stu_id in students:
            try:
                mark = float(input(f"Student {students[stu_id].id}'s mark: "))
            except ValueError:
                print("---------------------------")
                print("Please input number from 0 to 20 only!")
                print("---------------------------")
                print("Please wait for 1 second...")
                time.sleep(2)
                # os.system("cls")
                clear()
                input_marks(students, courses)

            if mark < 0 or mark > 20:
                print("---------------------------")
                print("Please input number from 0 to 20 only!")
                print("---------------------------")
                print("Please wait for 1 second...")
                time.sleep(2)
                # os.system("cls")
                clear()
                input_marks(students, courses)
            # Create a new mark object
            new_mark = {
                "student": students[stu_id],
                "course": courses[cou_id],
                "mark": mark
            }
            # Add the mark object to the dictionary
            marks[(stu_id, cou_id)] = new_mark
        print("-----------------")

        # Write the mark information to the file
        SavePickleThread(marks, "marks.pkl").start()

    if len(marks) != 0:
        print("Database of student has been imported!")
        return marks
    else:
        print("Check the code!")
        return marks