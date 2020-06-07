from tkinter import*
root=Tk()
import tkinter.messagebox as mb
import mysql.connector
import os
import runpy

p=PhotoImage()

def checking():
    db=mysql.connector.connect(host="localhost",user="root",password="evneet1234",database="evneet")
    cursor=db.cursor()
    name=e1.get()
    roll_no=e2.get()
    course=e3.get()
    if(name=='' or roll_no=='' or course==''):
        mb.showwarning("warning","All Fields must be filled out!!!")
    else:
        cursor.execute("select * from student_info where name ='%s' and roll_no='%d'and course='%s'"%(name,int(roll_no),course))
        rows=cursor.fetchone()
        if(rows!=2):
           global p
           p=PhotoImage(file=rows[10])
           mb.showinfo("info","welcome")
           top=Toplevel()
                
           top.geometry("650x650+150+20")
           top.resizable(False,False)
           top.config(background="black")
          
           l=Label(top,image=p)
           l.place(x=380,y=100,width=265,height=300)
        
           head=Label(top,text="WELCOME TO P.M.N COLLEGE",width=30,font=20,bg="sky blue",fg="navy blue",bd=10,relief="groove")
           head.place(x=100,y=0)
           l1=Label(top,text="Name",bd=10,relief="groove",bg="black",fg="red",font=20,width=15)
           l1.place(x=10,y=80)
           l2=Label(top,text=rows[0],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
           l2.place(x=200,y=80)
           l3=Label(top,text="Roll-No",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
           l3.place(x=10,y=150)
           l10=Label(top,text=roll_no,width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
           l10.place(x=200,y=150)
                 
           l4=Label(top,text="Course",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
           l4.place(x=10,y=220)
           l5=Label(top,text=rows[1],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
           l5.place(x=200,y=220)
           l6=Label(top,text="Father-Name",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
           l6.place(x=10,y=290)
           l7=Label(top,text=rows[4],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
           l7.place(x=200,y=290)
           l8=Label(top,text="Mother-Name",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
           l8.place(x=10,y=360)
           l9=Label(top,text=rows[5],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
           l9.place(x=200,y=360)
           l10=Label(top,text=rows[0],bd=10,relief="groove",bg="black",fg="red",font=20,width=15)
           l10.place(x=450,y=410)
        
           
                

                 
        else:
           mb.showwarning("warning","your name and your roll_No are not found please fill your valid rollno")
    db.close
root.geometry("500x500+200+200")
root.resizable(False,False)
root.config(background="black")
head=Label(root,text="Student Verification",width=20,font="arial 25 bold",relief='groove',bd=10,bg="grey",fg="red")
head.place(x=40,y=0)
l=Label(root,text="Student Name",bg="black",fg="orange",font="arial 15 bold",relief='groove',bd=10,width=15)
l.place(x=10,y=80)
def validateName(event):
    name=e1.get()
    if(event.char.isalpha()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass
    else:
        mb.showwarning("warning","plase enter only characters")
        e1.delete(0,'end')
        e1.insert(0,name[0:len(name)-1])


e1=Entry(root,width=25,bd=10,relief='groove')
e1.place(x=250,y=80)
e1.bind('<KeyRelease>',validateName)

l2=Label(root,text="Roll-No",bg="black",fg="orange",font="arial 15 bold",relief='groove',bd=10,width=15)
l2.place(x=10,y=150)
def validateRoll(event):
    roll_no=e2.get()
    if(event.char.isdigit()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass
    else:
        mb.showwarning("warning","plase enter only digits value")
        e2.delete(0,'end')
        e2.insert(0,roll_no[0:len(roll_no)-1])

e2=Entry(root,width=25,bd=10,relief='groove')
e2.place(x=250,y=150)
e2.bind('<KeyRelease>',validateRoll)


l3=Label(root,text="Course",bg="black",fg="orange",font="arial 15 bold",relief='groove',bd=10,width=15)
l3.place(x=10,y=220)
def validateCourse(event):
    Class=e3.get()
    if(event.char.isalpha()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass
    else:
        mb.showwarning("warning","plase enter only characters")
        e3.delete(0,'end')
        e3.insert(0,Course[0:len(Course)-1])

e3=Entry(root,width=25,bd=10,relief='groove')
e3.place(x=250,y=220)
e3.bind('<KeyRelease>',validateCourse)

bt=Button(root,text="Click For Checking--->",bg="black",fg="green",font="arial 15 bold",relief='groove',bd=10,command=checking)
bt.place(x=120,y=300)
def home():
 root.destroy()
 runpy.run_module('main_page')

bt4=Button(root,text="<--Back-To-HOME",bg="black",fg="green",font="arial 15 bold",relief="groove",bd=10,command=home)
bt4.place(x=5,y=400)

root.mainloop()
