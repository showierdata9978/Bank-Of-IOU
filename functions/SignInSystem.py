
def signinsystem(JustCreatedAccount,Bank,message,prompt) : 
     
    
    from functions.Bank import bank
    from replit import db
    
    
    
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
            return
        return
    
    elif prompt == "sign in":
        Username = input("Username : ")
        pasword = input("pasword : ")
        message.update(pasword.encode())
        Hashedpasword = message
        bank(Hashedpasword, Username, JustCreatedAccount, Bank)

        return
  