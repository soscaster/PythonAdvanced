# -*- coding: utf-8 -*-

import curses
import math
import numpy as np
import os
clear = lambda: os.system('clear')

screen = curses.initscr()

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit


class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark


class Manage:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.screen = curses.initscr()

    def input_students(self):
        self.screen.clear()
        self.screen.addstr("----- WELCOME -----")
        self.screen.refresh()
        self.screen.addstr("Number of students you want to import: ")
        self.screen.refresh()
        stunum = int(self.screen.getstr())
        i = 0
        for _ in range(stunum):
            i = i + 1
            self.screen.addstr("Let's input information for Student No. " + str(i))
            self.screen.refresh()
            self.screen.addstr("Student ID: ")
            self.screen.refresh()
            stu_id = str(self.screen.getstr())
            self.screen.addstr("Student name: ")
            self.screen.refresh()
            stu_name = str(self.screen.getstr())
            self.screen.addstr("Student DOB: ")
            self.screen.refresh()
            stu_dob = str(self.screen.getstr())            
            student = Student(stu_id, stu_name, stu_dob)
            self.students[stu_id] = student

            self.screen.addstr("Student No. " + str(i) + " information has been imported successfully!")

    def input_courses(self):

        self.screen.addstr("Number of courses you want to import: ")
        self.screen.refresh()
        cou_num = int(self.screen.getstr())
        i = 0

        for i in range(cou_num):
            i = i + 1
            self.screen.addstr("Let's input information for Course No. " + str(i))
            self.screen.addstr("Course ID: ")
            self.screen.refresh()
            cou_id = str(self.screen.getstr())
            self.screen.addstr("Course name: ")
            self.screen.refresh()
            cou_name = str(self.screen.getstr())
            self.screen.addstr("Course credit(s): ")
            self.screen.refresh()
            cou_credit = int(self.screen.getstr())
            course = Course(cou_id, cou_name, cou_credit)
            self.courses[cou_id] = course

            self.screen.addstr("Course No. " + str(i) + " information has been imported successfully!")

    def list_all(self):
        self.screen.addstr("Input completed! ")
        self.screen.addstr("List of courses: ")

        for cou_id in self.courses:
            self.screen.addstr("ID: " + str(self.courses[cou_id].id) + ", Course Name: " + str(self.courses[cou_id].name) + ", Course Credit(s): " + str(self.courses[cou_id].credit))
        
        self.screen.addstr("List of students: ")
        for stu_id in self.students:
            self.screen.addstr("ID: " + str(self.students[stu_id].id) + ", Name: " + str(self.students[stu_id].name) + ", DOB: " + str(self.students[stu_id].dob))

    def input_marks(self):
        self.screen.addstr("Please input the course ID you want to input mark: ")
        self.screen.refresh()
        cou_id = str(self.screen.getstr())        
        if cou_id in self.courses:
            self.screen.addstr("Course found!")
            self.screen.addstr("Course ID: " + str(self.courses[cou_id].id) + ", Course name: " + str(self.courses[cou_id].name))

            for stu_id in self.students:
                self.screen.addstr("Student ID: " + str(self.students[stu_id].id) + ", Student name: " + str(self.students[stu_id].name))
                self.screen.addstr("Please input the mark: ")
                self.screen.refresh()
                mark = float(self.screen.getstr())
                if mark >= 0 and mark <= 20:
                    key = (stu_id, cou_id)
                    mark = math.floor(mark)
                    markre = Mark(stu_id, cou_id, mark)
                    self.marks[stu_id] = markre
                    self.screen.addstr("Mark information has been imported successfully!")
                else:
                    self.screen.addstr("Invalid mark!")
                    self.screen.addstr("Please input the mark again!")
                    self.input_marks()

            else:
                self.screen.addstr("Student not found!")
        else:
            self.screen.addstr("Course not found!")

    def show_marks(self):
        clear()
        self.screen.addstr("Please input the course ID you want to show mark: ")
        self.screen.refresh()
        cou_id = str(self.screen.getstr())
        if cou_id in self.courses:
            self.screen.addstr("Course found!")
            self.screen.addstr("Course ID: " + str(self.courses[cou_id].id) + ", Course name: " + str(self.courses[cou_id].name))
            self.screen.addstr("List of marks: ")

            for stu_id in self.marks:
                mark = self.marks[stu_id]
                if mark.course == cou_id:
                    self.screen.addstr("Student ID: " + str(mark.student) + ", Mark (rounded): " + str(mark.mark))
            self.continue_or_not()
        else:
            self.screen.addstr("Course not found!")

    def gpa_calculator(self):
        clear()
        self.screen.addstr("Please input the student ID you want to calculate GPA: ")
        self.screen.refresh()
        stu_id = str(self.screen.getstr())
        if stu_id in self.students:
            self.screen.addstr("Student found!")
            self.screen.addstr("Student ID: " + str(self.students[stu_id].id) + ", Student name: " + str(self.students[stu_id].name))

            marks = []

            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)

            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    credits.append(self.courses[mark.course].credit)

            gpa = np.average(marks, weights=credits)
            self.screen.addstr("GPA: " + str(gpa))
            self.continue_or_not_sort()
        else:
            self.screen.addstr("Student not found!")

    def sort_by_gpa(self):
        clear()
        self.screen.addstr("Sort by GPA descending order")
        gpa = {}

        for stu_id in self.students:
            marks = []
            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)
                    credits.append(self.courses[mark.course].credit)
            gpa[stu_id] = np.average(marks, weights=credits)

        gpa = dict(sorted(gpa.items(), key=lambda item: item[1], reverse=True))

        for stu_id in gpa:
            self.screen.addstr("Student ID: " + str(stu_id) + ", GPA: " + str(gpa[stu_id]))
        exit()

    def continue_or_not(self):
        while True:
            self.screen.addstr("Do you want to continue? (Y/N): ")
            self.screen.refresh()
            continue_or_not = str(self.screen.getstr())
            
            if continue_or_not == "Y":
                self.show_marks()
            
            elif continue_or_not == "N":
                self.gpa_calculator()
            
            else:
                self.screen.addstr("Please input Y or N!")

    def continue_or_not_sort(self):
        while True:
            self.screen.addstr("Do you want to continue? (Y/N): ")
            self.screen.refresh()
            continue_or_not = str(self.screen.getstr())
            
            if continue_or_not == "Y":
                self.gpa_calculator()
            
            elif continue_or_not == "N":
                self.sort_by_gpa()
            
            else:
                self.screen.addstr("Please input Y or N!")

manage = Manage()
clear()
manage.input_students()

print("Please wait for 3 seconds...")
import time
time.sleep(3)
clear()

manage.input_courses()

print("Please wait for 3 seconds...")
time.sleep(3)
clear()

manage.list_all()
manage.input_marks()
while True:
    screen.addstr("-----------------")
    screen.addstr("Input mark for the course completed!")
    screen.addstr("Do you want to continue with other course? (Y/N)")
    screen.addstr("Your choice: ")
    screen.refresh()
    choice = str(screen.getstr())
    if choice == "Y":
        manage.input_marks()
    elif choice == "N":
        manage.show_marks()
    else:
        screen.addstr("Invalid choice. Please try again!")
        continue
    