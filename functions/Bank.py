def bank(Hashedpasword, username, JustCreatedAccount, Bank):
  import hashlib
  message = hashlib.sha256()
  from replit import db
  

  if Hashedpasword == db[username] : 
    if JustCreatedAccount:
          AmmountOfIOU = 200
          JustCreatedAccount = False
    bankhash = Bank + username + Hashedpasword
    bankhash = message.update(bankhash.encode())      
    db[bankhash] = AmmountOfIOU
    print(AmmountOfIOU)
  else:
        print("wrong username or pasword")
