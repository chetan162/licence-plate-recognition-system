from tkinter import *
from PIL import Image
from PIL import ImageTk
import sqlite3
import requests


con=sqlite3.connect('rto.db')
cor=con.cursor()
var1='HR26DK8337'

z=8
s=0
def red():
    global z
    z=1
def yellow():
    global z
    z=1
def green():
    global z
    z=0
def close():
    light.destroy()
def close1():
    global s
    s=txt2.get("1.0","end-1c")
    speed.destroy()

light=Tk()
light.geometry("400x170")
light.title("select light")
label1=Label(light,text="SELECT TRAFFIC LIGH COLOR",fg='blue',bg='yellow',relief="solid",font=("arial",15,"bold")).grid(row=0,column=1)
btn1=Button(light,text="RED",fg='red',bg='red',command=red)
btn2=Button(light,text="YELLOW",fg='yellow',bg='yellow',command=yellow)
btn3=Button(light,text="__GREEN__ ",fg='green',bg='green',command=green)
btn4=Button(light,text="OK",fg='brown',bg='white',font=("arial",15,"bold"),command=close)
btn1.grid(row=1,column=0)
btn2.grid(row=2,column=0)
btn3.grid(row=3,column=0)
btn4.grid(row=4,column=1)
light.mainloop()

speed =Tk()
speed.geometry("400x170")
speed.title("input speed")
label1=Label(speed,text="Input speed",fg='blue',bg='yellow',relief="solid",font=("arial",15,"bold")).grid(row=0,column=1)
txt2=Text(speed,width=20,height=2,wrap=WORD)
txt2.grid(row=1,column=1)
btn5=Button(speed,text="OK",fg='brown',bg='white',font=("arial",15,"bold"),command=close1)
btn5.grid(row=3,column=1)
speed.mainloop()


if z==1:
    t='red/yellow'
else:
    t='green'
def show():
    
    
    
    
    window.destroy()
window=Tk()

window.geometry("1020x1020")
window.title("welcome")
frame1=Frame(window,width=250,height=320,bg='red')
label1=Label(window,text="welcome to rto window",fg='blue',bg='yellow',relief="solid",font=("arial",25,"bold")).grid(row=0,column=1)

photo=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
photo1=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
photo2=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")
photo3=PhotoImage(file="C:/Users/CHETAN KUMAR/Desktop/test 1.PNG")


label7=Label(window,image=photo)
label8=Label(window,image=photo1)
label9=Label(window,image=photo2)
label10=Label(window,image=photo3)

label7.grid(row=1,column=0)
label8.grid(row=1,column=1)
label9.grid(row=1,column=2)
label10.grid(row=1,column=3)



label2=Label(window,text="NO_PLATE :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label3=Label(window,text="NAME :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label4=Label(window,text="MOBILE_NO :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label5=Label(window,text="ADDRESS :",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label6=Label(window,text="light signal:",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label15=Label(window,text="speed:",fg='brown',bg='white',relief="solid",font=("arial",12,"normal"))
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)
label4.grid(row=4,column=0)
label5.grid(row=5,column=0)
label6.grid(row=6,column=0)
label15.grid(row=7,column=0)




cor.execute("select * from rto where noplate=?", (var1,) )
data=cor.fetchone()
b1=data[0]
b2=data[1]
b3=data[2]
b4=data[3]
label11=Label(window,text=str(b1),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label12=Label(window,text=str(b2),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label13=Label(window,text=str(b3),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label14=Label(window,text=str(b4),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label16=Label(window,text=(str(t)),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label17=Label(window,text=(str(s)+" km/hr"),fg='black',relief="solid",font=("arial",12,"normal"),borderwidth=0)
label11.grid(row=2,column=1)
label12.grid(row=3,column=1)
label13.grid(row=4,column=1)
label14.grid(row=5,column=1)
label16.grid(row=6,column=1)
label17.grid(row=7,column=1)



btn=Button(window,text="send_info",width=20,height=4,font=("arial",20,"bold"),fg='brown',bg='white',command=show)
btn.grid(row=9,column=1)

con.close()
window.mainloop()