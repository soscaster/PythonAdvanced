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


# Khai bao dictionary chua cac thong tin
students = {}
courses = {}
marks = {}

# Cac ham nhap thong tin
def input_students():
  # Nhap so luong sinh vien can nhap
  num_students = int(input("Enter number of students: "))

  # Nhap thong tin sinh vien
  for _ in range(num_students):
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_DoB = input("Enter student date of birth: ")
    students[student_id] = {"id": student_id, "name": student_name, "dob": student_DoB}

def input_courses():
  # Nhap so luong mon hoc can nhap
  num_courses = int(input("Enter number of courses: "))

  # Nhap thong tin mon hoc
  for _ in range(num_courses):
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses[course_id] = {"id": course_id, "name": course_name}

# Ham nhap diem cho tung sinh vien theo tung course
def input_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        mark = float(input(f"Enter the mark for {students[student_id]['name']}: "))
        if student_id not in marks.keys():
            marks[student_id] = {}
        marks[student_id][course_id] = mark

# Ham hien thi danh sach cac course
def list_courses():
    for course_id in courses:
        print(f"{courses[course_id]['id']}: {courses[course_id]['name']}")

# Ham hien thi danh sach cac sinh vien
def list_students():
    for student_id in students:
        print(f"{students[student_id]['id']}: {students[student_id]['name']}, DOB: {students[student_id]['dob']}")

# Ham hien thi diem cua tung sinh vien theo tung course
def show_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['name']}: N/A")

# Chay chuong trinh, chay hai ham nhap thong tin truoc khi chay menu
input_students()
input_courses()

# Menu chinh
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

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