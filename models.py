
class User:
    def __init__(self):
        self.name = None 
        self.email = None
        self.user_id = None
    
    def display(self):
        pass


class Student:
    def __init__(self, email, name, student_id,major):
        self.name = name 
        self.email = email
        self.student_id = student_id
        self.major = major 

    def new_dict(self) ->dict:
        return{
            "name": self.name,
            "student_id": self.student_id,
            "email": self.email,
            "major" : self.major, 
        }


    def from_dict(cls, data: dict):
        return cls(
            student_id=data.get("student_id"),
            name=data.get("name"),
            age=data.get("age"),
            major=data.get("major"),
            email=data.get("email"),
        )
    
        
    def  display(self):
        print(f"Student ID: {self.student_id}, \n Name: {self.name}, \n Email: {self.email}, \n Major: {self.major  } \n is created successfully")
        