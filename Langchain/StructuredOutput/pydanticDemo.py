from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Jyoti'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='Represent Cgpa')
newStudent = {'name':'Deeksha', 'age': '24', 'email':'abc@gmila.com','cgpa':2}   
student = Student(**newStudent)
print(student)
studentDict = dict(student)
print(studentDict['age'])
studentJson = student.model_dump_json()
print(studentJson)