from tkinter import *
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
    print (int(z))
    light.destroy()
def close1():
    global s
    s=txt2.get("1.0","end-1c")
    print (s)
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