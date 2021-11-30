def dbsetup(key):
    global dbf
    global enc
    enc = key.encode
    dbf = open('functions/Database/db.dat')
    return enc

def read(key):
    ret = dbf.readline(key.encode())
    dbf.close()
    return ret


def write(data, key):
    count = len(dbf.readlines())
    while key.encode() < count or not key.encode() == count:
        open(dbf,'a')
        dbf.close()
    open(dbf, 'w')
    dbf.write(key.encode(), data)
    dbf.close()


def dele(key):
    open(dbf, 'w')
    dbf.write(" ", key.encode())
    dbf.close()


def reset(til):
    for i in range(1, til):
        open(dbf, 'w')
        dbf.write("", i)


def DB(data, key, func):
    dbsetup(key)
    if func == "w":
        write(data, key)
    elif func == "r":
        read(key)
    elif func == "re":
        reset(key)
    elif func == "d":
        dele(key)
    else:
        Error("no function nammed " + func, "functions/database/db.py.DB")
    return


def Error(why, where):
    print(why + "/n " + where)

    return
