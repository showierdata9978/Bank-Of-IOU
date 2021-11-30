def signinsystem(just_created_account, Bank, message, prompt, signed_in):

    from functions.Bank import bank
    from replit import db

    if not signed_in:
        if prompt == "sign up":
            username = "None"
            if db[username] == "None":
                username = input("username : ")
                pasword = input("pasword : ")
            message.update(pasword.encode())
            hashed_pasword = message
            if not db[username] == hashed_pasword:
                db[username] = hashed_pasword
                just_created_account = True

        elif prompt == "sign in":
            username = input("Username : ")
            pasword = input("pasword : ")
            message.update(pasword.encode())
            hashed_pasword = message
            bank(hashed_pasword, username, just_created_account, Bank,
                 signed_in)

    else:
        bank(hashed_pasword, username, just_created_account, Bank, signed_in)
    return
