from models import User, Student
from utils import normalize_name, is_valid_email, is_valid_age 





def main():
    student_id = input("Enter your student id: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    major = input ("Enter you major: ")
    email = input("Enter your email: ")
    
    #validating age and email and formatting name 

    if not is_valid_email(email):
        print("Invalid email")
        return
    if not is_valid_age (age):
        print("Invalid age")
        return
    name = normalize_name(name) 

    student_1 = Student(student_id, name, email, major)
    student_1.display()  

if __name__ == "__main__":
    main() 