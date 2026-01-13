
class User:
    def __init__(self):
        self.name = None 
        self.email = None
        self.user_id = None
    
    def display(self):
        pass


class Student:
    def __init__(self):
        self.name = None 
        self.email = None
        self.student_id = None
        self.major = None 
        
    def  display(self):
        print(f"Student ID: {self.student_id}, \n Name: {self.name}, \n Email: {self.email}, \n Major: {self.major  } \n is created successfully")
        