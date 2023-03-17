def input_students():
    print("----- WELCOME -----")

    # Input the number of students are going to be input
    stunum = int(input("Number of students you want to import: "))
    students = {}

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
        from domains.student import Student
        student = Student(stu_id, stu_name, stu_dob)
        # Add the student object to the dictionary
        students[stu_id] = student

        print("Student No.", i, " information has been imported successfully!")
        print("--------------------------------------------")
    return students

def input_courses():
    # Input the number of courses are going to be input
    cou_num = int(input("Number of courses you want to import: "))
    courses = {}

    # Set i = 0, then i = i+1 to create a loop to input the course information
    i = 0

    # Input the course information by using for loop and append the information to the dictionary
    for i in range(cou_num):
        i = i + 1
        print("Let's input information for Course No.", i)
        cou_id = str(input("Course ID: "))
        cou_name = str(input("Course name: "))
        cou_credit = int(input("Course credit(s): "))

        # Create a new course object
        from domains.course import Course
        course = Course(cou_id, cou_name, cou_credit)
        # Add the course object to the dictionary
        courses[cou_id] = course

        print("Course No.", i, " information has been imported successfully!")
        print("--------------------------------------------")
    return courses