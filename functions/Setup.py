import hashlib
from functions.SignInSystem import signinsystem
def mainFunc() :
  signinpromt()
  return
def signinpromt():

    global prompt
    prompt = input("sign in or sign up : ").lower()
    if prompt == "sign in" or "sign up":

        setup()
        signinsystem(JustCreatedAccount,Bank,message,prompt)
        return
    else:
        print("error: command not known ")
        return


def setup():
    global Bank   
    Bank = "IOU Bank"
    print(Bank)
    global JustCreatedAccount
    global message
    JustCreatedAccount = False
    message = hashlib.sha256()
    



