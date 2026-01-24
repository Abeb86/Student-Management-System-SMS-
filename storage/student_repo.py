import json
import os
from models import Student 
file_path = "data/students.json"
import pprint 

def to_json(student: Student):
    student_dict = {
        "name": student.name,
        "student_id": student.student_id,
        "major": student.major,
        "email": student.email
    }


    # 1) Read existing data (or initialize)
    if (not os.path.exists(file_path)) or os.stat(file_path).st_size == 0:
        data = []
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("students.json must contain a JSON array (list). Example: []")

    # 2) Add new student
    data.append(student_dict)

    # 3) Write back (overwrite file)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def to_dict():
    if not os.path.exists(file_path):
        print("The file does not exist")
        return None 

    with open (file_path, "r", encoding ="utf-8") as file_dict:
            data = json.load(file_dict)
    return data 