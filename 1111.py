students = []


def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def get_marks(message="Enter marks: "):
    while True:
        try:
            marks = float(input(message))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name or not roll_no:
        print("Name and roll number cannot be empty.")
        return

    if find_student(roll_no):
        print("A student with this roll number already exists.")
        return

    marks = get_marks()

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n--- Student List ---")
    print(f"{'Roll No':<12}{'Name':<25}{'Marks'}")
    print("-" * 45)

    for student in students:
        print(f"{student['roll_no']:<12}{student['name']:<25}{student['marks']}")


def search_student():
    roll_no = input("Enter roll number to search: ").strip()
    student = find_student(roll_no)

    if student:
        print("\nStudent Found!")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ").strip()
    student = find_student(roll_no)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")

    new_name = input(f"Enter new name [{student['name']}]: ").strip()
    new_marks = input(f"Enter new marks [{student['marks']}]: ").strip()

    if new_name:
        student["name"] = new_name

    if new_marks:
        try:
            marks = float(new_marks)

            if 0 <= marks <= 100:
                student["marks"] = marks
            else:
                print("Marks were not updated: they must be between 0 and 100.")

        except ValueError:
            print("Marks were not updated: invalid value.")

    print("Student updated successfully!")


def delete_student():
    roll_no = input("Enter roll number to delete: ").strip()
    student = find_student(roll_no)

    if not student:
        print("Student not found.")
        return

    confirm = input(f"Delete {student['name']}? (yes/no): ").lower()

    if confirm == "yes":
        students.remove(student)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")