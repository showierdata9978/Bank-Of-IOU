def dbsetup(key):
    global dbf
    global dbp 
    dbp = 'functions/Database/db.dat'
    
    mBytes = key.encode("utf-8")
    inc = int.from_bytes(mBytes, byteorder="big")
    dbf = open(dbp)
    return inc
    count = len(dbp.readlines())
    while not count >= 5: 
     write(" ",5)
def read(inc):
    ret = dbf.readline(inc)
    dbf.close()
    return ret


def write(data, inc):
    count = len(dbf.readlines())
    while inc < count or not inc == count:
        open(dbp, 'a')
        dbf.close()
    open(dbp, 'w')
    dbf.write(int(inc,2), data)
    dbf.close()


def dele(inc):
    open(dbp, 'w')
    dbf.write(" ", inc)
    dbf.close()


def reset(til):
    for i in range(2, til):
        open(dbp, 'w')
        dbf.write("", i)


def DB(data, key, func):
    inc = dbsetup(key)
    print(inc)
    if func == "w":
        write(data, inc)
    elif func == "r":
        ret = read(inc)
        return ret
    elif func == "re":
        reset(inc)
    elif func == "dele":
        dele(inc)
    else:
        Error("no function nammed " + func, "functions/database/db.py.DB")
    


def Error(why, where):
    print(why,2 + "/n " + where)

    return
