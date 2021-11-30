def signinpromt(just_created_account, bank, message, signed_in):

    if not signed_in:
        from functions.SignInSystem import signinsystem
        prompt = input("sign in or sign up : ").lower()
        if prompt == "sign in" or "sign up":

            signinsystem(just_created_account, bank, message, prompt,signed_in)

        else:
            print("error: command not known ")

    else:
        signinsystem(just_created_account, bank, message, prompt, signed_in)
    return
