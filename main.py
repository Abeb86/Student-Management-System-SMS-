from models import User, Student
from utils import normalize_name, is_valid_email, is_valid_age
from service.student_service import create_students 
def main():
   create_students()  

if __name__ == "__main__":
    main() 