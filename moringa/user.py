# class User:
#     def __init__(self,name,phone,email):
#         self.name  = name
#         self.phone = phone
#         self.email = email
        
#     def send_message(self,message):
#         print(message)


# class Admin(User):
#     def __init__(self, name, phone, email,admin_email):
#         super().__init__(name, phone, email)
#         self.admin_email = admin_email
        
#     def create_cohort(self,cohort_name):
#         print(cohort_name,"was created by ",self.name)

#     def create_user(self,user:User):
#         print(user.name,"was created by ",self.name)
students = [
    {
    "name":"clement ann",
     "phone":"0712 ccc ccc",
     "email":"vvv@gmail.com",
     "student_email":"ccc@student.com",
     },
     {
    "name":"clement kamau",
     "phone":"0712 vvv ccc",
     "email":"vvv@gmail.com",
     "student_email":"vvv@student.com",
     },
      {
    "name":"clement jane",
     "phone":"0712 vvv ccc",
     "email":"vvvv@gmail.com",
     "student_email":"ccc@student.com"
     },
       {
    "name":"clement kariuki",
     "phone":"0712 vvv ccc",
     "email":"vvvv@gmail.com",
     "student_email":"vvv@student.com"
     },
]
for student in students:
    # print(student["name"])
    student = Student(name=student["name"],email=student["email"],
                      phone=student["phone"],student_email=student["student_email"])
    
    student.send_message("we have an upcoming project")