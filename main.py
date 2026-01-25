from service.student_service import (
    create_students,
    getStudent,
    displayAll,
    updateStudent,
    deleteStudent
)

def main():
    while True:
        print("\n====== Student Management System ======")
        print("1. Create student")
        print("2. Display all students")
        print("3. Get student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        try:
            value = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value == 1:
            create_students()

        elif value == 2:
            displayAll()

        elif value == 3:
            try:
                student_id = int(input("Enter student ID: ").strip())
                getStudent(student_id)
            except ValueError:
                print("Invalid ID.")

        elif value == 4:
            try:
                student_id = int(input("Enter student ID: ").strip())
                updateStudent(student_id)
            except ValueError:
                print("Invalid ID.")

        elif value == 5:
            try:
                student_id = int(input("Enter student ID: ").strip())
                deleteStudent(student_id)
            except ValueError:
                print("Invalid ID.")

        elif value == 6:
            print("Exiting system. Goodbye 👋")
            break

        else:
            print("Invalid option. Choose between 1 and 6.")

if __name__ == "__main__":
    main()
