# class Tm 
from .user import User
from .student import Student
class TM(User):
    
    def __init__(self, name, phone, email,work_email):
        super().__init__(name, phone, email)
        self.work_email = work_email
        
    def assign_student(self,student:Student):
        print(student.name,"was assigned to ",self.name)