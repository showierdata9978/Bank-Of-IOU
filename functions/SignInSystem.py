   
def signinsystem(JustCreatedAccount,Bank,message,prompt) : 
     
    
    from functions.Bank import bank
    from replit import db
    
    
    Username = input("Username : ")
    if prompt == "sign up":
        if db[Username] == "None":
            pasword = input("pasword : ")
        message.update(pasword.encode())
        HashedPas = message
        if not db[Username] == HashedPas:
            db[Username] = HashedPas
            JustCreatedAccount = True
            return
        return

    elif prompt == "sign in":
        pasword = input("pasword : ")
        message.update(pasword.encode())
        HashedPas = message
        bank(HashedPas, Username, JustCreatedAccount, Bank)

        return
  