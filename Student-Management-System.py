from datetime import date

# Data storage
students = {}
courses = {}
student_courses = {}
student_grades = {}
student_attendance = {}

# Register a new student
def register_student(student_id, name, age, student_class):
    if student_id not in students:
        students[student_id] = {"name": name, "age": age, "class": student_class}
        student_courses[student_id] = []
        student_grades[student_id] = {}
        student_attendance[student_id] = {}
        print(f"Student {name} registered successfully!")
    else:
        print(f"Student with ID {student_id} already exists.")

# Add a new course
def add_course(course_code, course_name):
    if course_code not in courses:
        courses[course_code] = course_name
        print(f"Course {course_name} added successfully!")
    else:
        print(f"Course {course_code} already exists.")

# Assign a course to a student
def assign_course(student_id, course_code):
    if student_id in students and course_code in courses:
        if course_code not in student_courses[student_id]:
            student_courses[student_id].append(course_code)
            student_grades[student_id][course_code] = None
            student_attendance[student_id][course_code] = []
            print(f"Assigned course {courses[course_code]} to {students[student_id]['name']}.")
        else:
            print(f"Course {courses[course_code]} already assigned to {students[student_id]['name']}.")
    else:
        print("Invalid student ID or course code.")

# Add grades for a student's course
def add_grade(student_id, course_code, grade):
    if student_id in students and course_code in student_courses[student_id]:
        student_grades[student_id][course_code] = grade
        print(f"Added grade {grade} for {students[student_id]['name']} in {courses[course_code]}.")
    else:
        print(f"Cannot add grade, invalid student ID or course not assigned.")

# Mark attendance for a course
def mark_attendance(student_id, course_code, attendance_date, status):
    if student_id in students and course_code in student_courses[student_id]:
        student_attendance[student_id][course_code].append({"date": attendance_date, "status": status})
        print(f"Marked attendance for {students[student_id]['name']} in {courses[course_code]} on {attendance_date}.")
    else:
        print(f"Cannot mark attendance, invalid student ID or course not assigned.")

# View report card
def generate_report_card(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"\nReport Card for {student['name']} (Class {student['class']})")
        print("-" * 40)
        print(f"{'Course':<20}{'Grade':<10}{'Attendance':<10}")
        for course_code in student_courses[student_id]:
            course_name = courses[course_code]
            grade = student_grades[student_id].get(course_code, "N/A")
            attendance = sum(1 for att in student_attendance[student_id][course_code] if att['status'] == "Present")
            print(f"{course_name:<20}{grade:<10}{attendance} days")
    else:
        print(f"No student found with ID {student_id}")

# Main menu for the Student Management System
def student_management_system():
    while True:
        print("\n---- STUDENT MANAGEMENT SYSTEM ----")
        print("1. Register a Student")
        print("2. Add a Course")
        print("3. Assign Course to Student")
        print("4. Add Grade for Student")
        print("5. Mark Attendance")
        print("6. Generate Report Card")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            student_class = input("Enter Student Class: ")
            register_student(student_id, name, age, student_class)
        elif choice == "2":
            course_code = input("Enter Course Code: ")
            course_name = input("Enter Course Name: ")
            add_course(course_code, course_name)
        elif choice == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            assign_course(student_id, course_code)
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            add_grade(student_id, course_code, grade)
        elif choice == "5":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            attendance_date = date.today()
            status = input("Enter Attendance Status (Present/Absent): ")
            mark_attendance(student_id, course_code, attendance_date, status)
        elif choice == "6":
            student_id = input("Enter Student ID: ")
            generate_report_card(student_id)
        elif choice == "7":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the Student Management System
if __name__ == "__main__":
    student_management_system()
