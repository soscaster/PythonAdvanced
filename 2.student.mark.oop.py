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
                mark = str(input("Please input the mark: "))
                
                # Create a new mark object
                mark = Mark(stu_id, cou_id, mark)
                # Add the mark object to the dictionary
                self.marks[stu_id] = mark

                # One more way to add the mark information to the dictionary
                # marks[stu_id] = {"id": stu_id, "course": cou_id, "mark": mark}

                print("Mark information has been imported successfully!")
                print("--------------------------------------------")
            else:
                print("Student not found!")

        else:
            print("Course not found!")

        # One more way to input the mark information
        # cou_id = str(input("Enter the course ID you want to input mark: "))
        # if cou_id not in courses:
        #     print("Cannot find the course ID. Please try again!")
        #     return
        # for stu_id in students:
        #     mark = float(input(f"Mark of {students[stu_id]['name']}: "))
        #     if stu_id not in marks:
        #         marks[stu_id] = {}
        #     marks[stu_id][cou_id] = mark


        # One even more way to input the mark information
        # # Input the number of marks are going to be input
        # mark_num = int(input("Number of marks you want to import: "))

        # # Set i = 0, then i = i+1 to create a loop to input the mark information
        # i = 0

        # # Input the mark information by using for loop and append the information to the dictionary
        # for i in range(mark_num):
        #     i = i + 1
        #     print("Let's input information for Mark No.", i)
        #     stu_id = str(input("Student ID: "))
        #     cou_id = str(input("Course ID: "))
        #     mark = str(input("Mark: "))

        #     # Create a new mark object
        #     mark = Mark(stu_id, cou_id, mark)
        #     # Add the mark object to the dictionary
        #     self.marks[stu_id] = mark

        #     # One more way to add the mark information to the dictionary
        #     # marks[stu_id] = {"id": stu_id, "course": cou_id, "mark": mark}

        #     print("Mark No.", i, " information has been imported successfully!")
        #     print("--------------------------------------------")

    # Output the mark for each student in each course (choose the course first, then choose the student)
    def show_marks(self):
        cou_id = str(input("Please input the course ID you want to show mark: "))
        if cou_id in self.courses:
            print("Course found!")
            print("Course name: ", self.courses[cou_id].name)
            print("----------------------------")
            stu_id = str(input("Please input the student ID you want to show mark: "))
            if stu_id in self.students:
                print("Student found!")
                print("Student name: ", self.students[stu_id].name)
                print("----------------------------")
                print("Mark: ", self.marks[stu_id].mark)
                print("--------------------------------------------")
                self.continue_or_not()
            else:
                print("Student not found!")

        else:
            print("Course not found!")

    # One more way to output the mark information
    # cou_id = str(input("Enter the course ID you want to show mark: "))
    # if cou_id not in courses:
    #    print("Cannot find the course ID. Please try again!")
    #   return
    # for stu_id in students:
    #    if stu_id in self.marks:
    #       print(f"Mark of {students[stu_id]['name']}: {marks[stu_id][cou_id]}")
    # else:
    #   print(f"Mark of {students[stu_id]['name']}: Not Found / Not Available")
    # print("--------------------------------------------")       

    # Create a function to ask if the user wants to continue or not
    def continue_or_not(self):
        while True:
            # Ask the user if they want to continue or not
            continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.show_marks()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                print("Thank you for using our program!")
                exit()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                print("Please input Y or N!")

    # One more way to create a function to ask if the user wants to continue or not
    # def continue_or_not(self):
    # show_marks()
    # print("-----------------")
    # print("Do you want to continue with other course? (Y/N)")
    # choice = input("Your choice: ")
    # if choice == "Y":
    #     show_marks()
    # elif choice == "N":
    #     print("Thank you for using our program!")
    #     exit()
    # else:
    #     print("Invalid choice. Please try again!")

# Run the program
manage = Manage()
import os
os.system("cls")
manage.input_students()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
import time
time.sleep(3)
os.system("cls")

# Continue
manage.input_courses()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
time.sleep(3)
os.system("cls")

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
