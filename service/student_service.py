import pprint
from models import Student
from utils import normalize_name, is_valid_email, is_valid_age
from storage.student_repo import to_dict, save_data

def create_students():
    student_id = input("Enter your student id: ").strip()
    name = input("Enter your name: ").strip()
    major = input("Enter your major: ").strip()
    email = input("Enter your email: ").strip()

    if not is_valid_email(email):
        print("Invalid email")
        return False

    name = normalize_name(name)

    students = to_dict()

    # Duplicate ID check
    for s in students:
        if str(s.get("student_id")) == str(student_id):
            print(f"Student ID {student_id} already exists.")
            return False

    new_student = Student(student_id=student_id, name=name,  major=major, email=email)
    students.append(new_student.new_dict())
    save_data(students)

    print("Student created successfully.")
    return True


def displayAll():
    data = to_dict()
    if not data:
        print("There is no one registered.")
        return

    for student in data:
        pprint.pprint(student)


def getStudent(student_id: int):
    data = to_dict()
    if not data:
        print("No data is found")
        return None

    if not isinstance(data, list):
        raise ValueError("students.json must be a JSON array (list)")

    for student in data:
        if not isinstance(student, dict):
            raise ValueError(f"Invalid record, got {type(student)}: {student}")

        if int(student.get("student_id")) == int(student_id):
            pprint.pprint(student)
            return student

    # only after loop
    print(f"The student with id {student_id} doesn't exist")
    return None

def updateStudent(student_id: int):
    data = to_dict()
    if not data:
        print("No data found.")
        return False

    for student in data:
        if int(student.get("student_id")) == int(student_id):
            name = input("Enter new name: ").strip()
            major = input("Enter new major: ").strip()
            email = input("Enter new email: ").strip()

            if not is_valid_email(email):
                print("The email is not valid.")
                return False

            student["name"] = normalize_name(name)
            student["major"] = major
            student["email"] = email

            save_data(data)  # persists the full list
            print(f"Student with id {student['student_id']} has been updated.\n")
            return True

    print(f"Student with id {student_id} not found.")
    return False
from storage.student_repo import to_dict, save_data

def deleteStudent(student_id: int) -> bool:
    students = to_dict()

    if not students:
        print("No students found.")
        return False

    # search for the student
    for index, student in enumerate(students):
        if int(student.get("student_id")) == int(student_id):
            removed = students.pop(index)   # remove from list
            save_data(students)              # persist change

            print(f"Student with id {removed['student_id']} has been deleted.")
            return True

    print(f"Student with id {student_id} not found.")
    return False
