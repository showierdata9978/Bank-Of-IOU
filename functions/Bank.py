def bank(Hashedpasword, username, JustCreatedAccount, Bank, SignedIn):
    from functions.Database.Db import DB
    import hashlib
    message = hashlib.sha256()
    from replit import db
    db = DB("null",username,"r")
    if Hashedpasword == db or SignedIn:
        SignedIn = False
        if JustCreatedAccount:
            AmmountOfIOU = 200
            JustCreatedAccount = False
        bankhash = Bank + username + Hashedpasword
        bankhash = message.update(bankhash.encode())
        db[bankhash] = AmmountOfIOU
        print(AmmountOfIOU)
    else:
        print("wrong username or pasword")
