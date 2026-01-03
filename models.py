from utils import normalize_name, is_valid_email, is_valid_age 

class User:
    def __init__(self, user_id, name, email):
        self.name = name
        self.email = email
        self.user_id = user_id
    
    def display(self):
        pass

class Student:
    def __init__(self, student_id, name, email, major):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.major = major
        
    def  display(self):
        
        if not is_valid_email(self.email):
            print("Invalid email")
            return 
        self.name = normalize_name(self.name)  
        print(f"Student ID: {self.student_id}, \n Name: {self.name}, \n Email: {self.email}, \n Major: {self.major  }")
        