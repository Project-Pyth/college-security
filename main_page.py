from tkinter import*
import os
import tkinter.messagebox as mb
import threading
import importlib
import runpy

root=Tk()
root.geometry("600x600+10+60")
root.resizable(False,False)
root.config(background="sky blue")
p=PhotoImage(file="pmn.1.png")
l=Label(root,image=p)
l.place(x=0,y=50,width=600)

l1=Label(width=150,bg="pink",height=3)
l1.place(x=0,y=0)



def register():
  root.destroy()
  runpy.run_module('add_student')
 
bt=Button(l1,text="REGISTRATION",bg="pink",fg="navy blue",font="arial 15 bold",relief="groove",bd=6,width=15,command=register)
bt.place(x=0,y=0)
   
def checking():
 t=threading.Thread(target=open_camera)
 t.start()
 bt2.config(state=DISABLED)

def open_camera():
  runpy.run_module('face')
  bt2.config(state=NORMAL)      

bt2=Button(l1,text= "CHECKING ",bg="pink",fg="navy blue",font="arial 15 bold",relief="groove",bd=6,command=checking,width=15)
bt2.place(x=200,y=0)


def searching():
  root.destroy()
  runpy.run_module('searching_page')


bt3=Button(l1,text= "Details ",bg="pink",fg="navy blue",font="arial 15 bold",relief="groove",bd=6,command=searching,width=15)
bt3.place(x=400,y=0)

l2=Label(width=150,bg="pink",height=3)
l2.place(x=0,y=550)

def help():
   root.destroy()
   runpy.run_module('help_page')

bt4=Button(l2,text= "Help",bg="pink",fg="navy blue",font="arial 15 bold",relief="groove",bd=5,command=help,width=10)
bt4.place(x=0,y=0)


def logout():
  b=mb.askyesno("confirmation","you want to exit")
  if(b):
   root.destroy()
   runpy.run_module('front_page')

bt5=Button(l2,text= "LOGOUT",bg="white",fg="black",font="arial 15 bold",relief="groove",bd=5,command=logout,width=10)
bt5.place(x=460,y=0)


root.mainloop()



