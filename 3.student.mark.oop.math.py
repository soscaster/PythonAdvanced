# -*- coding: utf-8 -*-

# CLAIM: This code is written by myself, without copying from any other sources.
# I started to write this code from Monday, 6 March 2023, 20:13:47
# and the last modified is at the time I commit all.
# If you find any similarities with other sources, trust me, it's just a coincidence.
# I struggled a lot at most of the functions, and I can't input the student
# marks at the same time. So I have to use the old-school method is to input the marks
# for each student of each course. I'm sorry for that.
# May the Buddha bless you and me.

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
import numpy as np
import os
import time
# This code is for Windows : os.system("cls")
clear = lambda: os.system('clear')

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

    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    # The student input function definition
    def input_students(self):
        print("----- WELCOME -----")

        # If stunum is not a number, then the program will ask you to input again using try catch
        try:
            # Input the number of students are going to be input
            stunum = int(input("Number of students you want to import: "))
        except ValueError:
            print("---------------------------")
            print("Please input numbers only!")
            print("---------------------------")
            print("Please wait for 1 second...")
            time.sleep(2)
            # os.system("cls")
            clear()
            self.input_students()

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
        # If cou_num is not a number, then the program will ask you to input again using try catch
        try:
            # Input the number of courses are going to be input
            cou_num = int(input("Number of courses you want to import: "))
        except ValueError:
            print("---------------------------")
            print("Please input numbers only!")
            print("---------------------------")
            print("Please wait for 1 second...")
            time.sleep(2)
            # os.system("cls")
            clear()
            self.input_courses()
        
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

        # Set i = 0, then i = i+1 to create a loop to input the course information
        i = 0

        # Input the course information by using for loop and append the information to the dictionary
        for i in range(cou_num):
            i = i + 1
            print("Let's input information for Course No.", i)
            cou_id = str(input("Course ID: "))
            cou_name = str(input("Course name: "))

            # If cou_credit is not a number, then the program will ask you to input again using try catch
            try:
                cou_credit = int(input("Course credit(s): "))
            except ValueError:
                print("---------------------------")
                print("Please input numbers only!")
                print("---------------------------")
                print("Please wait for 1 second...")
                time.sleep(2)
                # os.system("cls")
                clear()
                self.input_courses()

            # If cou_credit is less than 0, then the program will ask you to input again
            if cou_credit < 0:
                print("---------------------------")
                print("Please input positive number only!")
                print("---------------------------")
                print("Please wait for 1 second...")
                time.sleep(2)
                # os.system("cls")
                clear()
                self.input_courses()

            # Create a new course object
            course = Course(cou_id, cou_name, cou_credit)
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
            print(f"ID: {self.courses[cou_id].id}, Course Name: {self.courses[cou_id].name}, Course Credit(s): {self.courses[cou_id].credit}")
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
                if mark >= 0 and mark <= 20:
                    key = (stu_id, cou_id)
                    # math.floor is used to round the mark to 1 decimal place
                    mark = math.floor(mark * 10) / 10
                    # Create a new mark object
                    markre = Mark(stu_id, cou_id, mark)
                    # Add the mark object to the dictionary
                    self.marks[key] = markre

                # One more way to add the mark information to the dictionary
                # self.marks[stu_id] = {"id": stu_id, "course": cou_id, "mark": mark}

                    print("Mark information has been imported successfully!")
                    print("--------------------------------------------")
                else:
                    
                    print("Invalid mark!")
                    print("Please input the mark again!")
                    print("--------------------------------------------")
                    # Show the mark input menu again
                    self.input_marks()
            else:
                print("Student not found!")

        else:
            print("Course not found!")


    def show_marks(self):
        clear()
        cou_id = str(input("Please input the course ID you want to show mark: "))
        if cou_id in self.courses:
            print("--------------------------------------------")
            print("Course found!")
            print("Course name: ", self.courses[cou_id].name)
            print("----------------------------")
            print("List of marks: ")

        # Iterate over the marks dictionary and display the marks for the specified course
            for stu_id in self.marks:
                mark = self.marks[stu_id]
                if mark.course == cou_id:
                    print(f"Student ID: {mark.student}, Mark (rounded): {mark.mark}")
            print("----------------------------")
            self.continue_or_not()
        else:
            print("Course not found!")

    # Calculate the GPA for each student (choose the student first)
    # using math and numpy modules
    def gpa_calculator(self):
        clear()
        stu_id = str(input("Please input the student ID you want to calculate GPA: "))
        if stu_id in self.students:
            print("Student found!")
            print("Student name: ", self.students[stu_id].name)
            print("----------------------------")

            # Calculate the GPA using numpy
            marks = []

            # Get the marks for the specified student
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)

            # Get course credits for the specified student
            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    credits.append(self.courses[mark.course].credit)

            # Calculate the GPA
            # GPA = (sum of marks*credit)/sum of credit
            gpa = np.average(marks, weights=credits)


            print(f"GPA: {gpa}")
            print("--------------------------------------------")
            self.continue_or_not_sort()
        else:
            print("Student not found!")

    # Sort student list by GPA descending order
    def sort_by_gpa(self):
        clear()
        print("Sort by GPA descending order")
        print("----------------------------")

        # Create a new dictionary to store the GPA
        gpa = {}

        # Calculate the GPA for each student
        for stu_id in self.students:
            marks = []
            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)
                    credits.append(self.courses[mark.course].credit)
            gpa[stu_id] = np.average(marks, weights=credits)

            # math.floor is used to round the GPA to 1 decimal place
            # gpa[stu_id] = math.floor(gpa[stu_id] * 10) / 10

        # Sort the GPA dictionary by GPA descending order
        gpa = dict(sorted(gpa.items(), key=lambda item: item[1], reverse=True))

        # Print the sorted GPA dictionary
        for stu_id in gpa:
            print(f"Student ID: {stu_id}, GPA: {gpa[stu_id]}")
        print("--------------------------------------------")
        self.survey()

    # Create a function to ask if the user wants to continue or run GPA count function
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

    # Create a function to ask if the user wants to continue or run sort GPA function
    def continue_or_not_sort(self):
        while True:
            # Ask the user if they want to continue or not
            continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.gpa_calculator()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                self.sort_by_gpa()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                print("Please input Y or N!")

    # Create a function to do a survey using yes/no questions
    def survey(self):
        while True:
            # Ask the user if they happy with the program or not
            happy = str(input("Are you happy with the program? (Y/N): "))

            # If the user inputs Y, then the program will stop
            if happy == "Y":
                print("---------------------------")
                print("Thank you for using the program!")
                print("Made by: Nguyen Quang Minh - BI12-271")
                exit()

            # If the user inputs N, then the program will ask the user to input again
            elif happy == "N":
                print("Please input your feedback below:")
                feedback = str(input("Feedback: "))
                # If the feedback includes curse words like "fuck", then curse him
                curse_words = ["4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses", "assfucker", "assfukka", "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch", "ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner", "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum", "bunny fucker", "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink", "cipa", "cl1t", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead", "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", "cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", "cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate", "f u c k", "f u c k e r", "f4nny", "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck", "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker", "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked", "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme", "fucks", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "fux", "fux0r", "f_u_c_k", "gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned", "goddamn", "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", "homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", "jizz", "kawk", "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust", "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "masochist", "master-bate", "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking", "mothafuckings", "mothafucks", "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nazi", "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "p0rn", "pawn", "pecker", "penis", "penisfucker", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", "rectum", "retard", "rimjaw", "rimming", "s hit", "s.o.b.", "sadist", "schlong", "screwing", "scroat", "scrote", "scrotum", "semen", "sex", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", "shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", "snatch", "son-of-a-bitch", "spac", "spunk", "s_h_i_t", "t1tt1e5", "t1tties", "teets", "teez", "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt", "twunter", "v14gra", "v1gra", "vagina", "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy", "xrated", "xxx"]
                if feedback in curse_words:
                    print("Oh yeah? Guess what? F*** you too buddy!")
                    exit()
                else:
                    print("---------------------------")
                    print("Actually we don't care but thank you for your feedback XD")
                    exit()

            # If the user inputs other characters, then the program will ask the user to input again
            else:
                print("Please input Y or N!")




manage = Manage()
clear()
manage.input_students()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
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
    print("Do you want to continue with other course/student? (Y/N)")
    choice = input("Your choice: ")
    if choice == "Y":
        manage.input_marks()
    elif choice == "N":
        manage.show_marks()
    else:
        print("Invalid choice. Please try again!")
        continue
