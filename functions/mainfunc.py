from functions.Signinprompt import signinpromt
from functions.Setup import setup


def main_func(SignedIn):
    setup()
    from functions.Setup import just_created_account, bank, message
    signinpromt(just_created_account, bank, message, SignedIn)
    return
