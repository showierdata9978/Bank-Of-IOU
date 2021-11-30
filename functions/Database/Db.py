def dbsetup(key):
    global dbf
    global dbp 
    dbp = 'functions/Database/db.dat'
    
    mBytes = key.encode("utf-8")
    inc = int.from_bytes(mBytes, byteorder="big")
    dbf = open(dbp)
    print(dbf)
    print(inc)
    print(mBytes)
    
    count = len(dbp.readlines())
    while not count >= 5: 
     write(" ",5)
    return inc
def read(inc):
    
    
    ret = dbf.readline()
    print(ret)
    ret = ret.decode
    print(ret)
    dbf.close()
    return ret


def write(data, inc):
    count = len(dbf.readlines())
    print(count)
    while inc < count or not inc == count:
        open(dbp, 'a')
        dbf.close()
    open(dbp, 'w',inc)
    dbf.write(int(inc,2), data)
    dbf.close()


def dele(inc):
    open(dbp, 'w',inc)
    dbf.write(" ", inc)
    dbf.close()


def reset(til):
    for i in range(2, til):
        open(dbp, 'w')
        dbf.write("", i)

def clear():
   count = len(dbp.readlines())
   while not count == 1 : 
    count = len(dbp.readlines())
    dbf.write(" ",count)

def DB(data, key, func):
    inc = dbsetup(key)
    print(data)
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
