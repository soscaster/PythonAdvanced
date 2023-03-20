from domains.course import Course
from domains.student import Student
import numpy as np
import math

def display_students(students):
    print("List of students: ")
    for student_id, student in students.items():
        print(f"ID: {student_id}, Name: {student.name}, DOB: {student.dob}")
    print("-----------------")

def display_courses(courses):
    print("List of courses: ")
    for course_id, course in courses.items():
        print(f"ID: {course_id}, Name: {course.name}, Credits: {course.credit}")
    print("-----------------")

def display_marks(marks):
    print("List of marks: ")
    for key, mark in marks.items():
        student = mark['student']
        course = mark['course']
        mark_value = mark['mark']
        print(f"Student ID: {student.id}, Student Name: {student.name}, Course: {course.name}, Mark: {mark_value}")
    print("-----------------")



# Display GPA of all students in descending order
def display_gpa(marks):
    print("List of GPA in descending order: ")

    # Create a new dictionary to store the GPA
    gpa = {}

    # Calculate the GPA for each student using numpy
    for key in marks:
        mark = marks[key]
        student = mark['student']
        course = mark['course']
        mark_value = mark['mark']
        if student.id in gpa:
            gpa[student.id]['marks'].append(mark_value)
            gpa[student.id]['credits'].append(course.credit)
        else:
            gpa[student.id] = {'marks': [mark_value], 'credits': [course.credit]}
    for stu_id in gpa:
        gpa[stu_id]['id'] = stu_id
        # Round the GPA to 3 decimal places
        gpa[stu_id]['gpa'] = math.floor(np.average(gpa[stu_id]['marks'], weights=gpa[stu_id]['credits']) * 1000) / 1000

    # Sort the GPA dictionary by GPA descending order
    gpa = dict(sorted(gpa.items(), key=lambda item: item[1]['gpa'], reverse=True))

    # Print the sorted GPA dictionary
    for stu_id in gpa:
        print(f"Student ID: {gpa[stu_id]['id']}, GPA: {gpa[stu_id]['gpa']}")
    print("-----------------")
