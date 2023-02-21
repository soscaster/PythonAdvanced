# -*- coding: utf-8 -*-
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


# Declare the dictionaries will be used
students = {}
courses = {}
marks = {}

# Clear the screen
import os
os.system('clear')

# Input the student(s) list
def input_students():
    print("----- WELCOME -----")
  # Declare the number of students to be input
    stunum = int(input("Number of students you want to import: "))

  # Input the student(s) informations
    i = 0
    for _ in range(stunum):
        i = i+1
        print("Let's input information for Student No.",i)
        print("---------------------------")
        stu_id = str(input("Student ID: "))
        stu_name = str(input("Student name: "))
        stu_dob = str(input("Student DOB: "))
        # Add the student information to the dictionary
        students[stu_id] = {"id": stu_id, "name": stu_name, "dob": stu_dob}
        print("Student No.",i," information has been imported successfully!")
        print("--------------------------------------------")

def input_courses():
  # Declare the number of courses to be input
  cou_num = int(input("Number of courses you want to import: "))

  # Input the course information
  i = 0
  for i in range(cou_num):
    i = i+1
    print("Let's input information for Course No.",i)
    cou_id = str(input("Course ID: "))
    cou_name = str(input("Course name: "))
    # Add the course information to the dictionary
    courses[cou_id] = {"id": cou_id, "name": cou_name}
    print("Course No.",i," information has been imported successfully!")
    print("--------------------------------------------")

# List all the courses and students' information - ID, name, (DOB)

def list_all():
    print("Input completed!")
    print("List of courses: ")
    # Scan the dictionary and print the information
    for cou_id in courses:
        print(f"ID: {courses[cou_id]['id']}, Course Name: {courses[cou_id]['name']}")
    print("----------------------------")
    print("List of students: ")
    # Scan the dictionary and print the information
    for stu_id in students:
        print(f"ID: {students[stu_id]['id']}, Name: {students[stu_id]['name']}, DOB: {students[stu_id]['dob']}")
    print("--------------------------------------------")

# Input the marks for each student in each course
def input_marks():
    cou_id = str(input("Enter the course ID you want to input mark: "))
    if cou_id not in courses:
        print("Cannot find the course ID. Please try again!")
        return
    for stu_id in students:
        mark = float(input(f"Mark of {students[stu_id]['name']}: "))
        if stu_id not in marks:
            marks[stu_id] = {}
        marks[stu_id][cou_id] = mark

# Output the marks for each student in each course
def show_marks():
    cou_id = input("Enter the course ID you want to output: ")
    if cou_id not in courses:
        print("Cannot find the course ID. Please try again!")
        return
    for stu_id in students:
        if stu_id in marks and cou_id in marks[stu_id]:
            print(f"{students[stu_id]['name']}: {marks[stu_id][cou_id]}")
        else:
            print(f"{students[stu_id]['name']}: Not Found / Not Available")

# Create a function to ask the user if they want to continue with other course 
def show_marks_choise():
    show_marks()
    print("-----------------")
    print("Do you want to continue with other course? (Y/N)")
    choice = input("Your choice: ")
    if choice == "Y":
        show_marks()
    elif choice == "N":
        print("Thank you for using our program!")
        exit()
    else:
        print("Invalid choice. Please try again!")


# Run the program eventually
input_students()

# Wait for 3 seconds before clear the screen again
print("Please wait for 3 seconds...")
import time
time.sleep(3)
os.system('clear')

# Continue the program
input_courses()

# Wait for 3 seconds before clear the screen again
print("Please wait for 3 seconds...")
import time
time.sleep(3)
os.system('clear')

# Continue the program
list_all()
input_marks()
while True:
    print("-----------------")
    print("Input mark for the course completed.")
    print("Do you want to input other course? (Y/N)")
    choice = input("Your choice: ")
    if choice == "Y":
        input_marks()
    elif choice == "N":
        show_marks_choise()
    else:
        print("Invalid choice. Please try again!")
        continue

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
# THIỆN TAI - THIỆN TAI   `=--=-'        THIỆN TAI - THIỆN TAI
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Phật phù hộ, không bao giờ BUG
#            Nguyễn Quang Minh - ICT - BI12-271
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~