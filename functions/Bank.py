 
def bank(HashedPas,username,JustCreatedAccount,AmmountOfIOU,Bank):
      from replit import db
      if HashedPas == db[username]:
       if JustCreatedAccount :
        AmmountOfIOU = 200
        JustCreatedAccount = False 
       bankhash = Bank + username + HashedPas
       bankhash = bankhash.encode
       db[bankhash] = AmmountOfIOU
       print(AmmountOfIOU)
      else:
         print("wrong username or pasword") 
       
     