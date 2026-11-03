
students = []


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty. Please try again.")
        return

    while True:
        mark_input = input("Enter mark (0-100): ").strip()

        if not mark_input:
            print("Mark cannot be blank. Please try again.")
            continue

        try:
            mark = float(mark_input)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter a value between 0 and 100.")
            continue

        break

    grade = calculate_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"{name} added successfully! Grade: {grade}")


def show_results():
    if not students:
        print("No students added yet. Please add students first.")
        return

    print("\n" + "=" * 38)
    print(f"{'Name':<15}{'Mark':<10}{'Grade':<10}")
    print("=" * 38)

    marks = []

    for student in students:
        print(
            f"{student['name']:<15}"
            f"{student['mark']:<10.1f}"
            f"{student['grade']:<10}"
        )
        marks.append(student["mark"])

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("=" * 38)
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest:g}")
    print(f"Lowest: {lowest:g}")
    print("=" * 38)


def main():
    while True:
        print("\n===== GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thank you for using Grade Manager!")
            break
        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()

