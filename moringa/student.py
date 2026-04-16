# class student
from .user import User
class Student(User):
    def __init__(self,name,phone,email,student_email,cohort):
        super().__init__(name,phone,email)
        self.student_email = student_email
        self.cohort = cohort
        
    def mark_attedance(self,present:bool):
        if present:
            print(self.name,"was marked as present")
        else:
            print(self.name,"was marked as Absent")
        
        