from models import User, Student

student_id = input("Enter your student id: ")
name = input("Enter your name: ")
age = input("Enter your age: ")
major = input ("Enter you major: ")
email = input("Enter your email: ")

student_1 = Student(student_id, name, email, major)
student_1.display() 