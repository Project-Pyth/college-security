from tkinter import*
import runpy

root=Tk()
root.geometry("600x600+150+60")
root.resizable(False,False)
root.config(background="grey")
p=PhotoImage(file="college.png")
pic=Label(root,image=p)
pic.place(x=0,y=0,width=700,height=600)

l1=Label(pic,text="How May I Help You",bg="grey",fg="navy blue",font="arial 25 bold",relief="groove",bd=10,width=29)
l1.place(x=0,y=0)


l2=Label(pic,text= "Mailing Address:Evneetmudhar@gmail.com",bg="grey",fg="brown",font="arial 18 bold",relief="groove")
l2.place(x=20,y=150)
l3=Label(pic,text= "Contact Me On:",bg="grey",fg="brown",font="arial 18 bold underline")
l3.place(x=25,y=250)

l4=Label(pic,text= "9888450868:",bg="grey",fg="brown",font="arial 18 bold",width=11)
l4.place(x=25,y=285)

def home():
 root.destroy()
 runpy.run_module('main_page')
 
bt4=Button(root,text="<--Back-To-HOME",bg="black",fg="green",font="arial 15 bold",relief="groove",bd=10,command=home)
bt4.place(x=5,y=542)


root.mainloop()

