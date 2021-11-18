def bank():
       setup
       if HashedPas == db[username]:
         bankhash = Bank + username + HashedPas
         bankhash = bankhash.encode
         db[bankhash] = AmmountOfIOU
         print(AmmountOfIOU)
       else:
         print("wrong username or pasword") 
       
     