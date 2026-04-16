class User:
    def __init__(self,name,phone,email):
        self.name  = name
        self.phone = phone
        self.email = email
        
    def send_message(self,message):
        print(message)


class Admin(User):
    def __init__(self, name, phone, email,admin_email):
        super().__init__(name, phone, email)
        self.admin_email = admin_email
        
    def create_cohort(self,cohort_name):
        print(cohort_name,"was created by ",self.name)

    def create_user(self,user:User):
        print(user.name,"was created by ",self.name)