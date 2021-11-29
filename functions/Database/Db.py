
dbf = open('functions/Database/db.db')
def read(key):
 ret = dbf.readline(key.encode)
 return ret

def write(data,key) :
 count = len(open('functions/Database/db.db').readlines(  ))
 while key.encode < count or not key.encode == count:
   open('functions/Database/db.db','a')
   dbf.close()
 open('functions/Database/db.db','w')
 dbf.write(key.encode,data)

def clear(key):
  open('functions/Database/db.db','w')
  dbf.write(" ",key.encode)

def reset(til):
 for i in range(1,til):
   open('functions/Database/db.db','w')
   dbf.write("" ,i)
