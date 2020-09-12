import sqlite3

con=sqlite3.connect('rto.db')
cor=con.cursor()
var1='HR26DK8337'
cor.execute("select * from rto where noplate=?", (var1,) )
data=cor.fetchone()
b1=data[0]
b2=data[1]
b3=data[2]
b4=data[3]
print ("plate no "+str(b1))
print ("name "+str(b2))
print ("mobile no "+str(b3))
print ("address "+str(b4))
con.close()
