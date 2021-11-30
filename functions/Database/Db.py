def dbsetup(key):
    mBytes = key.encode("utf-8")
    inc = int.from_bytes(mBytes, byteorder="big")
    open('functions/Database/db.dat') 
    
    print(inc)
    print(mBytes)
    
    count = len(open('functions/Database/db.dat').readlines())
    while not count >= 5: 
     write(" ",5)
    return inc
def read(inc):
    
    
    ret = open('functions/Database/db.dat').readline(inc)
    
    ret = ret.decode
    open('functions/Database/db.dat').close()
    return ret


def write(data, inc):
    count = len(open('functions/Database/db.dat').readlines())
    print(count)
    while inc < count or not inc == count:
        open('functions/Database/db.dat', 'a')
        open('functions/Database/db.dat').close()
    open ('functions/Database/db.dat', 'w',inc)
    open('functions/Database/db.dat').write(data,int(inc,2))
    open('functions/Database/db.dat').close()


def dele(inc):
    open('functions/Database/db.dat', 'w',inc).write(" ")
   
    open('functions/Database/db.dat').close()


def reset(til):
    for i in range(2, til):
        open ('functions/Database/db.dat', 'w')
        open('functions/Database/db.dat').write("", i)

def clear():
   count = len(open('functions/Database/db.dat').readlines())
   while not count == 1 : 
    count = len(open('functions/Database/db.dat').readlines())
    open('D').write(" ",count)

def DB(data, key, func):
    inc = dbsetup(key)
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
        Error("no function nammed " + func, "functions/Database/db.py.DB")
    


def Error(why, where):
    print(why,2 + "/n " + where)

    return
