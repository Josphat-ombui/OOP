from .users import User

class Student(User):
    
    def __init__(self, name, email, phone,school_email):
        super().__init__(name, email, phone)
        self.school_email = school_email
        
    def send_attedance_warning(self):
        print(f'{self.name} you have been warned')
    