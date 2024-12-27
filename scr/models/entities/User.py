from werkzeug.security import generate_password_hash,check_password_hash



class User():
    
    def __init__(self,id, username, password, fullname = "" )-> None:

     self.id = id
     self.username = username
     self.password = password   
     self.fullname = fullname

    @classmethod
    def check_password(self,hashed_pasword,password):

      return check_password_hash (hashed_pasword,password)
   

   




