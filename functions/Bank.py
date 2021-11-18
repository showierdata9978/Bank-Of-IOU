 
def bank(HashedPas,username,JustCreatedAccount,Bank):
      import hashlib
      message = hashlib.sha256()
      from replit import db
      if HashedPas == db[username]:
       if JustCreatedAccount :
        AmmountOfIOU = 200
        JustCreatedAccount = False 
       bankhash = Bank + username + HashedPas
       bankhash = message.update(bankhash.encode())
       db[bankhash] = AmmountOfIOU
       print(AmmountOfIOU)
      else:
         print("wrong username or pasword") 
       
     