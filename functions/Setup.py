import hashlib
def setup():
    global bank   
    bank = "IOU Bank"
    print(bank)
    global _just_created_account
    global message
    _just_created_account = False
    message = hashlib.sha256()
    



