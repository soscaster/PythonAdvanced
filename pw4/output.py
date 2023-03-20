from domains.course import Course
from domains.student import Student

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
        print(f"Student: {student.name}, Course: {course.name}, Mark: {mark_value}")
    print("-----------------")
