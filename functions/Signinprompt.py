
def signinpromt(JustCreatedAccount,Bank,message,SignedIn):
 
  
  if not SignedIn :
    from functions.SignInSystem import signinsystem
    
    global prompt
    prompt = input("sign in or sign up : ").lower()
    if prompt == "sign in" or "sign up":

       
        signinsystem(JustCreatedAccount,Bank,message,prompt,SignedIn)
        return
    else:
        print("error: command not known ")
        return
        
  else : signinsystem(JustCreatedAccount,Bank,message,prompt,SignedIn)