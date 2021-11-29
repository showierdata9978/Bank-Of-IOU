from functions.Signinprompt import signinpromt
from functions.Setup import setup
def main_func() :
  setup()
  from functions.Setup import JustCreatedAccount,Bank,message
  signinpromt(JustCreatedAccount,Bank,message,)
  return
