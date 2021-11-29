import hashlib
def setup():
    global Bank   
    Bank = "IOU Bank"
    print(Bank)
    global JustCreatedAccount
    global message
    JustCreatedAccount = False
    message = hashlib.sha256()
    



