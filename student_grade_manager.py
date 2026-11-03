import json
import os

FILE_NAME = "students.json"

# Load student records
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save student records
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Add a student
def add_student():
    print("\n--- Add New Student ---")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    if any(s["roll_no"] == roll_no for s in students):
        print("Roll number already exists!")
        return

    subjects = ["English", "Maths", "Science", "Computer", "Social"]

    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks in {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks.values())
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")
    print(f"Total: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


# Display all students
def view_students():
    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n---------------------------")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("Total:", student["total"], "/500")
        print("Percentage:", f'{student["percentage"]:.2f}%')
        print("Grade:", student["grade"])


# Search for a student
def search_student():
    roll_no = input("\nEnter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Percentage:", f'{student["percentage"]:.2f}%')
            print("Grade:", student["grade"])
            return

    print("Student not found!")


# Main menu
students = load_students()

while True:
    print("\n==============================")
    print("     STUDENT GRADE MANAGER")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("\nThank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please try again.")

