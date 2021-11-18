import hashlib
from replit import db
def signinpromt() :
  
  global prompt
  prompt = input("sign in or sign up : ").lower()
  if prompt == "sign in" or "sign up":
    setup()
    return
  else: 
    print("error: command not known ")
    return
  
  


def setup():
     Bank = "IOU Bank"
    
     print(Bank)
     JustCreatedAccount = False
     message = hashlib.sha256()
     username = "username"
     pasword = "pasword"
     HashedPas = message.update(pasword.encode())
     
     username = input("Username : ")
     if prompt == "sign up" :
          if db[username] == "None" :  
           pasword = input("pasword : ")
          message.update(pasword.encode())
          HashedPas = message
          if not db[username] == HashedPas:
           db[username] = HashedPas   
           JustCreatedAccount = True 
           setup()
           return
          return
    
     elif prompt == "sign in":
         pasword = input("pasword : ")
         message.update(pasword.encode())
         HashedPas = message
         return
     
         
        
    
         