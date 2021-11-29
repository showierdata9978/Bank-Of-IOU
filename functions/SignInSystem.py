
def signinsystem(JustCreatedAccount,Bank,message,prompt,SignedIn) : 
     
    
    from functions.Bank import bank
    from replit import db
    
    
    if not SignedIn :
     if prompt == "sign up":
         Username = "None"
         if db[Username] == "None":
             Username = input("Username : ")
             pasword = input("pasword : ")
         message.update(pasword.encode())
         Hashedpasword = message
         if not db[Username] == Hashedpasword:
             db[Username] = Hashedpasword
             JustCreatedAccount = True
             
         
    
    
     elif prompt == "sign in":
         Username = input("Username : ")
         pasword = input("pasword : ")
         message.update(pasword.encode())
         Hashedpasword = message
         bank(Hashedpasword, Username, JustCreatedAccount, Bank,SignedIn)

         return
    else : 
      bank(Hashedpasword, Username, JustCreatedAccount, Bank,SignedIn)
      
    