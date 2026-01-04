
# Online Python - IDE, Editor, Compiler, Interpreter

def normalize_name(name:str)->str:
    name = name.strip()
    name = name.title()
    return name
    
def is_valid_email(email:str)->bool:
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.count("@") >1 and email.count("." )> 1:
        return False
    return True  
    

def is_valid_age(age:str)->bool:
    age = int(age)
    if age < 18 :
        return False
    if age > 100 :
        return False
    return True


