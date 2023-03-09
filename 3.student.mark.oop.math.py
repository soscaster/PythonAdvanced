# -*- coding: utf-8 -*-

# CLAIM: This code is written by myself, without copying from any other sources.
# I started to write this code from Monday, 6 March 2023, 20:13:47 and the last modified is at the time I save this comment.
# If you find any similarities with other sources, trust me, it's just a coincidence.
# I struggled a lot at the for loop and the Y/N function, and I can't display the student
# marks at the same time. But it's still working, for some reason...
# Maybe it's because of the power of Buddha.

#                            _
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/`---'\____
#                   .'  \\|     |//  `.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  `\`---'//  |_/ |
#                 \  .-\__ `-. -'__/-.  /
#               ___`. .'  /--.--\  `. .'___
#            ."" '<  `.___\_<|>_/___.' _> \"".
#           | | :  `- \`. ;`. _/; .'/ /  .' ; |
#           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
# ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
# THIEN TAI - THIEN TAI   `=--=-'        THIEN TAI - THIEN TAI
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Phật phù hộ, không bao giờ BUG
#            Nguyễn Quang Minh - ICT - BI12-271
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import math

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class Manage:

    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    # The student input function definition
    def input_students(self):
        print("----- WELCOME -----")

        # Input the number of students are going to be input
        stunum = int(input("Number of students you want to import: "))

        # Set i = 0, then i = i+1 to create a loop to input the student information
        i = 0

        # Input the student information by using for loop and append the information to the dictionary
        for _ in range(stunum):
            i = i + 1
            print("Let's input information for Student No.", i)
            print("---------------------------")
            stu_id = str(input("Student ID: "))
            stu_name = str(input("Student name: "))
            stu_dob = str(input("Student DOB: "))
            
            # Create a new student object
            student = Student(stu_id, stu_name, stu_dob)
            # Add the student object to the dictionary
            self.students[stu_id] = student

            # One more way to add the student information to the dictionary
            # students[stu_id] = {"id": stu_id, "name": stu_name, "dob": stu_dob}

            print("Student No.", i, " information has been imported successfully!")
            print("--------------------------------------------")

    def input_courses(self):
        # Input the number of courses are going to be input
        cou_num = int(input("Number of courses you want to import: "))

        # Set i = 0, then i = i+1 to create a loop to input the course information
        i = 0

        # Input the course information by using for loop and append the information to the dictionary
        for i in range(cou_num):
            i = i + 1
            print("Let's input information for Course No.", i)
            cou_id = str(input("Course ID: "))
            cou_name = str(input("Course name: "))

            # Create a new course object
            course = Course(cou_id, cou_name)
            # Add the course object to the dictionary
            self.courses[cou_id] = course

            # One more way to add the course information to the dictionary
            # courses[cou_id] = {"id": cou_id, "name": cou_name}

            print("Course No.", i, " information has been imported successfully!")
            print("--------------------------------------------")

    # List all the courses and students' information - ID, name, (DOB)
    def list_all(self):
        print("Input completed!")
        print("List of courses: ")
        
        # Scan the dictionary and print the information
        for cou_id in self.courses:
            print(f"ID: {self.courses[cou_id].id}, Course Name: {self.courses[cou_id].name}")
        print("----------------------------")
        print("List of students: ")

        # Scan the dictionary and print the information
        for stu_id in self.students:
            print(f"ID: {self.students[stu_id].id}, Name: {self.students[stu_id].name}, DOB: {self.students[stu_id].dob}")
        print("--------------------------------------------")

    # Input the mark for each student in each course (choose the course first, then choose the student)
    def input_marks(self):
        cou_id = str(input("Please input the course ID you want to input mark: "))
        
        # Check if the course ID is in the dictionary
        if cou_id in self.courses:
            print("Course found!")
            print("Course name: ", self.courses[cou_id].name)
            print("----------------------------")
            stu_id = str(input("Please input the student ID you want to input mark: "))
            
            # Check if the student ID is in the dictionary
            if stu_id in self.students:
                print("Student found!")
                print("Student name: ", self.students[stu_id].name)
                print("----------------------------")
                mark = float(input("Please input the mark: "))
                
                key = (stu_id, cou_id)

                # Round the mark using math.floor
                mark = math.floor(mark)

                # Create a new mark object
                markre = Mark(stu_id, cou_id, mark)

                # Add the mark object to the dictionary
                self.marks[key] = markre

                # One more way to add the mark information to the dictionary
                # self.marks[stu_id] = {"id": stu_id, "course": cou_id, "mark": mark}

                print("Mark information has been imported successfully!")
                print("--------------------------------------------")
            else:
                print("Student not found!")

        else:
            print("Course not found!")

    # Output the mark for each student in each course (choose the course first, then choose the student)
    # def show_marks(self):
    #     cou_id = str(input("Please input the course ID you want to show mark: "))
    #     if cou_id in self.courses:
    #         print("Course found!")
    #         print("Course name: ", self.courses[cou_id].name)
    #         print("----------------------------")
    #         stu_id = str(input("Please input the student ID you want to show mark: "))
    #         if stu_id in self.students:
    #             print("Student found!")
    #             print(f"{self.students[stu_id].name}: {self.marks[stu_id].mark}")
    #             print("--------------------------------------------")
    #             self.continue_or_not()
    #         else:
    #             print("Student not found!")
    #     else:
    #         print("Course not found!")

    def show_marks(self):
        cou_id = str(input("Please input the course ID you want to show mark: "))
        if cou_id in self.courses:
            print("Course found!")
            print("Course name: ", self.courses[cou_id].name)
            print("----------------------------")
            print("List of marks: ")

        # Iterate over the marks dictionary and display the marks for the specified course
            for stu_id in self.marks:
                mark = self.marks[stu_id]
                if mark.course == cou_id:
                    print(f"Student ID: {mark.student}, Mark (rounded): {mark.mark}")
            self.continue_or_not()
        else:
            print("Course not found!")

    # Calculate the GPA for each student (choose the student first)
    # using math and numpy modules
    def gpa_calculator(self):
        stu_id = str(input("Please input the student ID you want to calculate GPA: "))
        if stu_id in self.students:
            print("Student found!")
            print("Student name: ", self.students[stu_id].name)
            print("----------------------------")

            # Calculate the GPA using numpy
            import numpy as np
            marks = []

            # Get the marks for the specified student
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)
            
            # Calculate the GPA using numpy
            gpa = np.mean(marks)
            print(f"GPA: {gpa}")
            print("--------------------------------------------")
            self.continue_or_not_exit()
        else:
            print("Student not found!")

    # Create a function to ask if the user wants to continue or run another function
    def continue_or_not(self):
        while True:
            # Ask the user if they want to continue or not
            continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.show_marks()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                self.gpa_calculator()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                print("Please input Y or N!")



    # Create a function to ask if the user wants to continue or exit the program
    def continue_or_not_exit(self):
        while True:
            # Ask the user if they want to continue or not
            continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.gpa_calculator()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                print("Thank you for using our program!")
                exit()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                print("Please input Y or N!")

# Run the program
manage = Manage()
import os
# This code is for Windows : os.system("cls")
clear = lambda: os.system('clear')
clear()
manage.input_students()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
import time
time.sleep(3)
# os.system("cls")
clear()

# Continue
manage.input_courses()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
time.sleep(3)
# os.system("cls")
clear()

# Continue
manage.list_all()
manage.input_marks()
while True:
    print("-----------------")
    print("Input mark for the course completed!")
    print("Do you want to continue with other course? (Y/N)")
    choice = input("Your choice: ")
    if choice == "Y":
        manage.input_marks()
    elif choice == "N":
        manage.show_marks()
    else:
        print("Invalid choice. Please try again!")
        continue
