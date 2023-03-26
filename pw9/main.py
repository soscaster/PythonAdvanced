import sys
sys.dont_write_bytecode = True
from domains.course import Course
from domains.student import Student
from domains.mark import Mark
from input import input_student, input_courses, input_marks, load_students, load_courses, load_marks
from output import display_students, display_courses, display_marks, display_gpa
import zipfile
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import subprocess
import os
# Remember to change cls to clear if you're using Mac or Linux
clear = lambda: os.system('clear')
import time

# UTF-8 encoding for Vietnamese characters
os.environ['PYTHONIOENCODING'] = 'utf-8'


class Main:
    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

        # Check if students.dat exists
        if os.path.exists("students_pkl.dat"):
            clear()
            # hide the main window
            self.root = tk.Tk()
            self.root.withdraw()
            messagebox.showinfo("Notice", "The database is existed.\nPress OK to continue...")
            # Decompress and load data from it
            print("Decompressing files...")
            print("-----------------")
            with open("students_pkl.dat", "rb") as infile:
                with zipfile.ZipFile(infile, "r") as zipf:
                    zipf.extractall()
                    # Load data from extracted files
                    self.students = load_students()
                    self.courses = load_courses()
                    self.marks = load_marks(self.students, self.courses)
            print("Decompress files successfully!")
            print("-----------------")
            print("Please wait for a seconds...")
            time.sleep(1)
        else:
            clear()
            # hide the main window
            self.root = tk.Tk()
            self.root.withdraw()
            messagebox.showinfo("Notice", "The database is not existed yet.\nPress OK to continue...")
            print("The database is not existed yet. Normal mode initializing...")
            print("-----------------")
            print("Please wait for a seconds...")
            time.sleep(1)
        
        self.create_GUI()

    def create_GUI(self):
        root = tk.Tk()
        root.title("SMS - Nguyen Quang Minh - BI12-271")

        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=10)

        # Create widgets
        self.label = tk.Label(root, anchor='n', text="Student Management System", font=("Arial", 25), justify="center")
        add_student = tk.Button(root, text="Add student(s)", bg='#0052cc', fg='#ffffff')
        add_student["font"] = btn_font
        add_course_button = tk.Button(root, text="Add course(s)", bg='#0052cc', fg='#ffffff')
        add_course_button["font"] = btn_font
        display_stu_cou_button = tk.Button(root, text="Display students and courses", bg='#0052cc', fg='#ffffff')
        display_stu_cou_button["font"] = btn_font
        add_mark_button = tk.Button(root, text="Add mark(s)", bg='#0052cc', fg='#ffffff')
        add_mark_button["font"] = btn_font
        display_mark_button = tk.Button(root, text="Display marks", bg='#0052cc', fg='#ffffff')
        display_mark_button["font"] = btn_font
        display_gpa_button = tk.Button(root, text="Display GPA", bg='#0052cc', fg='#ffffff')
        display_gpa_button["font"] = btn_font
        exit_button = tk.Button(root, text="Exit", bg='#0052cc', fg='#ffffff')
        exit_button["font"] = btn_font

        # Bind events
        add_student.bind("<Button-1>", self.input_student)
        add_course_button.bind("<Button-1>", self.input_course)
        display_stu_cou_button.bind("<Button-1>", self.display_stu_cou)
        add_mark_button.bind("<Button-1>", self.input_mark)
        display_mark_button.bind("<Button-1>", self.display_mark)
        display_gpa_button.bind("<Button-1>", self.stu_gpa)
        exit_button.bind("<Button-1>", self.exit)

        # Layout widgets
        self.label.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        add_student.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        add_course_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        add_mark_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        display_stu_cou_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        display_mark_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        display_gpa_button.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)
        exit_button.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Set window size to be unchangeable
        root.resizable(False, False)

        # Start the GUI
        root.mainloop()

    def input_student(self, event=None):
        clear()
        # Input data for students
        if len (self.students) > 0:
            ask = messagebox.askyesno("Notice", "The student database is not empty.\nDo you want to overwrite it?")
            if ask:
                self.students = input_student(self)
                messagebox.showinfo("Result", "Input student data successfully!\nPress OK to continue...")
        else:
            self.students = input_student(self)
            messagebox.showinfo("Result", "Input student data successfully!\nPress OK to continue...")
    
    def input_course(self, event=None):
        clear()
        # Input data for courses
        if len (self.courses) > 0:
            ask = messagebox.askyesno("Notice", "The course database is not empty.\nDo you want to overwrite it?")
            if ask:
                self.courses = input_courses(self)
                messagebox.showinfo("Result", "Input course data successfully!\nPress OK to continue...")
        else:
            self.courses = input_courses(self)
            messagebox.showinfo("Result", "Input course data successfully!\nPress OK to continue...")

    def display_stu_cou(self, event=None):
        clear()
        if len (self.students) == 0 or len (self.courses) == 0:
            messagebox.showerror("Error", "The student or course database is empty.\nPlease input data first!\n\nOr if you encountered any problem when input student or mark, we suggest you to input it again.")
            return
        else:
            # Display data for students and courses
            display_students(self.students)
            display_courses(self.courses)
            messagebox.showinfo("Result", "The operation has been completed.")

    def input_mark(self, event=None):
        clear()
        # Input data for marks
        if len (self.marks) > 0:
            ask = messagebox.askyesno("Notice", "The mark database is not empty.\nDo you want to overwrite it?")
            if ask:
                self.marks = input_marks(self.students, self.courses)
                messagebox.showinfo("Result", "Input mark data successfully!\nPress OK to continue...")
        else:
            self.marks = input_marks(self.students, self.courses)
            messagebox.showinfo("Result", "Input mark data successfully!\nPress OK to continue...")

    def display_mark(self, event=None):
        clear()
        if len (self.marks) == 0:
            messagebox.showerror("Error", "The mark database is empty!\nPlease input mark data first.")
            return
        else:
            # Display data for marks
            display_marks(self.marks)
            messagebox.showinfo("Result", "The operation has been completed.")

    def stu_gpa(self, event=None):
        clear()
        if len (self.marks) == 0:
            messagebox.showerror("Error", "The mark database is empty!\nPlease input mark data first.")
            return
        else:
            # Display GPA of all students in descending order
            display_gpa(self.marks)
            messagebox.showinfo("Result", "The operation has been completed.")

    def exit(self, event=None):
        clear()
        # Compress all files txt into students.dat
        print("Compressing pkl files to students_pkl.dat ...")
        with open("students_pkl.dat", "wb") as outfile:
            with zipfile.ZipFile(outfile, "w") as zipf:
                for file in os.listdir():
                    if file.endswith(".pkl"):
                        zipf.write(file)
        print("Compress files successfully!")
        print("-----------------")

        # Delete the previous students.pkl file
        print("Deleting previous pickle files...")
        if os.path.exists("students.pkl"):
            os.remove("students.pkl")
        # Delete the previous courses.pkl file
        if os.path.exists("courses.pkl"):
            os.remove("courses.pkl")
        # Delete the previous marks.pkl file
        if os.path.exists("marks.pkl"):
            os.remove("marks.pkl")
        print("Delete files successfully!")
        print("-----------------")

        # Say goodbye
        messagebox.showinfo("Thank you!", "Compress file successfully!\nThank you for using the app!")

        # Exit
        exit()

if __name__ == "__main__":
    manage = Main()
    while True:
        manage.create_GUI()