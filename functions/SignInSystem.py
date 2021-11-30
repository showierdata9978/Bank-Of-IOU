from functions.Database.Db import DB
from functions.Bank import bank
    

def signinsystem(just_created_account, Bank, message, prompt, signed_in):
    
    
   
    if not signed_in:
        hashed_pasword = "set"
        username = "set"
        pasword = "set"
        if prompt == "sign up":
            username = " "
            pasword = "set"
            message.update(pasword.encode())
            hashed_pasword = message
            dbw = DB(hashed_pasword,username,"w")
            dbr3 = DB(hashed_pasword,username,"r")
            if dbr3 == " ":
                username = input("username : ")
                pasword = input("pasword : ")
            message.update(pasword.encode())
            hashed_pasword = message
            dbr = DB(hashed_pasword,username,"r")
            if not dbr == hashed_pasword:
                dbw = DB(hashed_pasword,username,"w")
                just_created_account = True

        elif prompt == "sign in":
            username = input("Username : ")
            pasword = input("pasword : ")
            
            message.update(pasword.encode())
            hashed_pasword = message
            DB(hashed_pasword,username,"r")
            bank(hashed_pasword, username, just_created_account, Bank,
                 signed_in)

    else:
        bank(hashed_pasword, username, just_created_account, Bank, signed_in)
    return
