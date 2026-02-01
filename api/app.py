from fastapi import FastAPI #importing the fastapi library
from storage.student_repo import to_dict, save_data
from .schemas import StudentCreate
app = FastAPI()  # creating the fastapi app 


@app.get("/health")
def health_check():
    return {"status":"ok",
    "message":"API is running"}  


@app.get("/students")
def get_students():
    students = to_dict()
    if not students:
        return {"error":"No students found"}
    return {"data":students, "status": "success"} 

    
@app.post("/students")
def create_Students(student: StudentCreate):
    students = to_dict()
    # Duplicate ID check
    for s in students:
        if str(s.get("student_id")) == str(student.student_id):
            return {"error":"Student ID already exists"}
        
    student_data = student.model_dump()
    students.append(student_data)
    save_data(students)
    return {"data":student_data, "status": "success"}