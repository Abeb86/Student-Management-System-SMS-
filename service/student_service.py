from models import Student
from utils import is_valid_email, is_valid_age, normalize_name
from storage.student_repo import to_json, to_dict, save_data
import pprint

def create_students():
    student_1 = Student()
    student_1.student_id = input("Enter your student id: ").strip()
    student_1.name = input("Enter your name: ").strip()
    student_1.age = input("Enter your age: ").strip()
    student_1.major = input("Enter your major: ").strip()
    student_1.email = input("Enter your email: ").strip()

    # validate
    if not is_valid_email(student_1.email):
        print("Invalid email")
        return False

    if not is_valid_age(student_1.age):
        print("Invalid age")
        return False

    student_1.name = normalize_name(student_1.name)

    # OPTIONAL Phase 2: prevent duplicate ID
    data = to_dict() or []
    for s in data:
        if str(s.get("student_id")) == str(student_1.student_id):
            print(f"Student ID {student_1.student_id} already exists.")
            return False

    # save (choose ONE approach)
    # If to_json already appends+persists, keep it:
    to_json(student_1)

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
