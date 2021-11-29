
def signinpromt(JustCreatedAccount,Bank,message,):
    from functions.SignInSystem import signinsystem
    global prompt
    prompt = input("sign in or sign up : ").lower()
    if prompt == "sign in" or "sign up":

       
        signinsystem(JustCreatedAccount,Bank,message,prompt)
        return
    else:
        print("error: command not known ")
        return
        
