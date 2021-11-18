from replit import db
import hashlib


#functions
def SignUp():
    setup()
    username = input("Username : ")
    if db[username] == "" :  
     pasword = input("pasword : ")
     message.update(pasword.encode())
    HashedPas = message
    if not db.prefix(username) == HashedPas:
        db[username] = HashedPas
        global JustCreatedAccount
        JustCreatedAccount = True
    
    else : print("there is already an accont with that user")
    return 

def setup():
    #makeing the vars
    global message
    global pasword
    global HashedPas
    global JustCreatedAccount
    global username
    global Bank
    global AmmountOfIOU
    #setting defult preamators
    JustCreatedAccount = False
    message = hashlib.sha256()
    username = "username"
    pasword = "pasword"
    HashedPas = message.update(pasword.encode())
    #defineing bank
    Bank = "IOU Bank"
    AmmountOfIOU = 24
    return


def Signin():

    setup()
    global username 
    username = input("Username : ")
    #loading and hashing pasword
    pasword = input("pasword : ")
    message.update(pasword.encode())
    global HashedPas 
    HashedPas = message

    return


def Bank():
    if HashedPas == db[username]:
        bankhash = Bank + username + HashedPas
        bankhash = bankhash.encode
        db[bankhash] = AmmountOfIOU
        print(AmmountOfIOU)
    else:
        print("wrong username or pasword")
        signinpromt()

    return


def signinpromt():
    #Signin / Signup prompt
    prompt1 = input("sign in or sign up : ").lower()
    if prompt1 == 'sign in':
        Signin()
    elif prompt1 == 'sign up':
        SignUp()
    else:
        print("error command not known ")


signinpromt()


Bank
   
print('test')

print("Your bank is done")
