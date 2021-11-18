from functions.Bank import bank
import hashlib
from replit import db
def signinpromt() :
  prompt = input("sign in or sign up : ").lower()
  if prompt == 'sign in' or 'sign up':
    setup()
  
  else: print("error command not known ")
  return 
  


def setup():
     
     #makeing the vars
     global message
     global pasword
     global HashedPas
     global JustCreatedAccount
     global username
     global Bank
     global AmmountOfIOU
     global prompt
     #setting defult preamators
     JustCreatedAccount = False
     message = hashlib.sha256()
     username = "username"
     pasword = "pasword"
     HashedPas = message.update(pasword.encode())
     #defineing bank
     print(HashedPas)
     Bank = "IOU Bank"
     AmmountOfIOU = 24
     username = input("Username : ")
     if prompt == "signup" :
          if db[username] == "None" :  
           pasword = input("pasword : ")
          message.update(pasword.encode())
          HashedPas = message
          if not db.prefix(username) == HashedPas:
           db[username] = HashedPas   
           JustCreatedAccount = True
           setup
         
         
     elif prompt == "signin":
       message.update(pasword.encode())
       HashedPas = message
       bank
     
         
        
     #Signin / Signup prompt
     

         