from tkinter import*
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from tkinter import ttk as tkk
import mysql.connector
import runpy

def login():
    db=mysql.connector.connect(host="localhost",user="root",password="evneet1234",database="evneet")
    cursor=db.cursor()
    user=e1.get()
    pwd=e2.get()
    if(user==None):
       mb.showwarning("warning","plase enter your user name")
    if(pwd==None):
       mb.showwarning("warning","plase enter your password name")
    if(user=='' or pwd==''):
        mb.showwarning("warning","All Fields must be filled out!!!")
   
    cursor.execute("select * from login where id='%s' and password='%s'"%(user,pwd))
    t2=cursor.fetchone()
    print(t2)
    if(t2!=None):
        mb.showinfo("info","welcome")
        root.destroy()
        runpy.run_module('main_page')
    else:
       mb.showwarning("warning","plase enter you valid user name and password")
       e1.delete(0,'end')
       e2.delete(0,'end')


    db.close()
                   
root=Tk()
root.geometry("500x500+150+60")
root.resizable(False,False)
root.config(background="sky blue")


l1=Label(root,text="Admin Login Panel",fg="blue",bg="white",width=25,font="arial 20 bold",relief='groove',bd=5)
l1.place(x=20,y=10)
l2=Label(root,text="Username",font="arial 15 bold",relief='groove',bd=5)
l2.place(x=50,y=90)
e1=Entry(root,width=30,bg="white",bd=10,relief='groove')
e1.place(x=50,y=130)
l3=Label(root,text="Password",font="arial 15 bold",relief='groove',bd=5)
l3.place(x=50,y=180)
e2=Entry(root,width=30,show="*",bg="white",bd=10,relief='groove')
e2.place(x=50,y=220)
bt1=Button(root,text="Login",fg="green",bg="white",width=10,font="arial 10 bold",relief='groove',bd=10,command=login)
bt1.place(x=50,y=300)
