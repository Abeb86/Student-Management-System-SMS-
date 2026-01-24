from models import User, Student
from utils import normalize_name, is_valid_email, is_valid_age
from service.student_service import create_students, getStudent
def main():
   print("choose One to create student\n")
   print("choose Two to display all student")

   value = int(input("Enter one value: "))
   if value == 1:
    create_students()
   elif value == 2:
      id = int(input( "Enter id: "))
      getStudent(id)  


if __name__ == "__main__":
    main() 