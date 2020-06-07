from tkinter import*
import runpy

root=Tk()
root.geometry("600x600+150+60")
root.resizable(False,False)
root.config(background="black")
p=PhotoImage(file="pmn.2.png")
l=Label(root,image=p)
l.place(x=0,y=0,width=650)

l1=Label(root,text="WELCOME TO P.M.N COLLEGE",bg="black",fg="red",font="arial 20 bold",relief="groove",bd=5)
l1.place(x=30,y=420)
l2=Label(root,text= "RAJPURA",bg="black",fg="red",font="arial 20 bold",relief="groove",bd=5)
l2.place(x=160,y=464)

def welcome():
 root.destroy()
 runpy.run_module('front_page')
 
bt=Button(root,text="NEXT-->",bg="sky blue",fg="green",font="arial 20 bold",relief="groove",bd=5,command=welcome)
bt.place(x=220,y=525)
 

 
