class User:
    def __init__(self,name,phone,email):
        self.name  = name
        self.phone = phone
        self.email = email
        
    def send_message(self,message):
        print(message)