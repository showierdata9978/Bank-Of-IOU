
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

def DB(data,key,func):
  if func == "W":
    write(data,key)
  elif func == "r" :
    read(key)
  elif func == "r":
    reset(key)
  elif func == "c" : 
   clear(key)
  else : 
    Error("nofuncnammed" + func , "functions/database/db.py.DB") 
  return

def Error(why,where):
  print(why + " " + where )
  
  return
    