from models import Student
from utils import is_valid_email, is_valid_age, normalize_name  
from storage.student_repo import to_json, to_dict
from storage.student_repo import file_path  
import json, pprint 



def create_students():
    student_1 = Student()
    student_1.student_id = input("Enter your student id: ")
    student_1.name = input("Enter your name: ")
    student_1.age = input("Enter your age: ")
    student_1.major = input ("Enter you major: ")
    student_1.email = input("Enter your email: ")
    
    #validating age and email and formatting name 
    if not is_valid_email(student_1.email):
        print("Invalid email")
        return
    if not is_valid_age (student_1.age):
        print("Invalid age")
        return
    student_1.name = normalize_name(student_1.name) 
    student_1.display()
    to_json(student_1)
    student_1.display() 
     #return the student object to the main function 

def getStudent(student_id:int):

        data = to_dict()
        if data is None:
            print("No data is found")
            return None
        
        if not isinstance(data, list):
            raise ValueError("student.json must be a JSON array")
        
        for student in data:
            if not isinstance(student, dict):
                raise ValueError(f"Invalid record, got {type(student):{student}}")

            if int(student.get("student_id"))==int(student_id):
                pprint.pprint(student)
                return student 
        

       

