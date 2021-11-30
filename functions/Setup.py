import hashlib


def setup():
    global bank
    bank = "IOU Bank"
    print(bank)
    global just_created_account
    global message
    just_created_account = False
    message = hashlib.sha256()
