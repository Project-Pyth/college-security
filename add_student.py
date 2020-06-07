from tkinter import*
from tkinter import ttk as ttk
import tkcalendar as cal
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import mysql.connector
import datetime
import os
import re
import runpy

filename=''

def new_student():
    global filename
    name=e1.get()
    rollno=e2.get()
    course=cbb.get()
    session2=cbb2.get()
    session3=cbb3.get()
    session=session2+"-"+session3
    fname=e4.get()
    mname=e5.get()
    dob=e6.get()
    gnd=""
    if n1.get()==1:
        gnd="Male"
    else:
        gnd="Female"

    email=e9.get()
    address=ta.get('1.0','end')
    db=mysql.connector.connect(host="localhost",user="root",password="evneet1234",database="evneet")
    cursor=db.cursor()
    directory=os.path.exists('student')
    if(directory==False):
        os.mkdir('student')
    pic_path='student/'+rollno+'.png'
    f=open(filename,'rb')
    data=f.read()
    f.close()
    f=open(pic_path,'wb')
    f.write(data)
    f.close()
    try:
        cursor.execute("insert into student_info(name,course,session,dob,father_name,mother_name,gender,email,address,roll_no,image)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%d','%s')"%(name,course,session,dob,fname,mname,gnd,email,address,int(rollno),pic_path))
        db.commit()
        mb.showinfo("Info","Student Info Addedd Successfully")
    except Exception as e:
         db.rollback()

         print("exception",e)
    db.close()
              
root=Tk()
root.geometry("650x650+150+20")
root.resizable(False,False)
root.config(background="sky blue")
head=Label(root,text="Student Registration",width=20,font="arial 23 bold",bd=5,relief='groove',bg="white",fg="red")
head.place(x=120,y=1)
l=Label(root,text="Student Name",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l.place(x=10,y=60)
def validatename(event):
    name=e1.get()
    if(event.char.isalpha()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass

    else:
        mb.showwarning("warning","plase enter only character values")
        e1.delete(0,'end')
        e1.insert(0,name[0:len(name)-1])



e1=Entry(root,width=25,bg="pink",bd=10,relief='groove')
e1.place(x=270,y=60)
e1.bind('<KeyRelease>',validatename)

l2=Label(root,text="Roll-No",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l2.place(x=10,y=100)
def validateRollNo(event):
    rno=e2.get()
    if(event.char.isdigit()):
        pass
    elif(event.char==''):
        pass

    else:
        mb.showwarning("warning","plase enter only numeric values")
        e2.delete(0,'end')
        e2.insert(0,rno[0:len(rno)-1])


        
e2=Entry(root,width=25,bg="pink",bd=10,relief='groove')
e2.place(x=270,y=100)
e2.bind('<KeyRelease>',validateRollNo)
l3=Label(root,text=" Course",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l3.place(x=10,y=140)
lst=['BCA','BBA','MCA','MBA','PGDCA','MSCIT']
cbb=ttk.Combobox(root,value=lst,width=25)
cbb.place(x=270,y=145)
cbb.set('MCA')
l11=Label(root,text="Session",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l11.place(x=10,y=180)
from_list=list(range(2000,2030))
cbb2=ttk.Combobox(root,value=from_list,width=11)
cbb2.place(x=270,y=182)
def calBatchTo(event):
    course=cbb.get()
    batch_from=cbb2.get()
    batch_to=0
    if course=='MCA':
        batchto=int(batch_from)+3
    elif course=='MBA':
        batchto=int(batch_from)+2
    elif course=='PGDCA':
        batchto=int(batch_from)+1
    elif course=='BBA':
        batchto=int(batch_from)+3
    elif course=='BCA':
        batchto=int(batch_from)+3
    elif course=='MSCIT':
        batchto=int(batch_from)+2
    
    cbb3.set(batchto)
        
cbb2.bind("<<ComboboxSelected>>",calBatchTo)

to_list=list(range(2003,2034))
cbb3=ttk.Combobox(root,value=to_list,width=11)
cbb3.place(x=355,y=182)

l6=Label(root,text="Date-of-birth",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l6.place(x=10,y=220)
e6=cal.DateEntry(root,width=10)
e6.place(x=270,y=220)

def get():
    d=e6.get()
    dob=datetime.datetime.strptime(d,'%m/%d/%y')
    curr_date=datetime.datetime.now()
    d2=str(curr_date.month)+"/"+str(curr_date.day)+"/"+str(curr_date.year)
    today_dd=datetime.datetime.strptime(d2,'%m/%d/%Y')
    diff=abs((today_dd-dob).days)
    age=round(diff//365)
    check.config(text=str(age) + "  -year ")

btcalender=Button(root,text="check your age",command=get,bg="sky blue",fg="green",font="arial 10 bold",relief='groove',bd=5,width=12)
btcalender.place(x=350,y=215)
check=Label(root,text=" ",width=12,bg="pink",fg="black",bd=5,relief='groove')
check.place(x=480,y=215)


l4=Label(root,text="Father-Name",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l4.place(x=10,y=260)
def validateFather(event):
    fname=e4.get()
    if(event.char.isalpha()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass

    else:
        mb.showwarning("warning","plase enter only characters")
        e4.delete(0,'end')
        e4.insert(0,fname[0:len(fname)-1])




e4=Entry(root,width=25,bg="pink",bd=10,relief='groove')
e4.place(x=270,y=260)
e4.bind('<KeyRelease>',validateFather)

l5=Label(root,text="Mother-Name",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l5.place(x=10,y=300)
def validateMother(event):
    mname=e5.get()
    if(event.char.isalpha()):
        pass
    elif(event.char==' '):
        pass
    elif(event.char==''):
        pass

    else:
        mb.showwarning("warning","plase enter only characters")
        e5.delete(0,'end')
        e5.insert(0,mname[0:len(mname)-1])

e5=Entry(root,width=25,bg="pink",bd=10,relief='groove')
e5.place(x=270,y=300)
e5.bind('<KeyRelease>',validateMother)

l7=Label(root,text="Gender",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l7.place(x=10,y=350)
n1=IntVar()
rb1=Radiobutton(root,text="Male",variable=n1,relief='groove',bd=5,value=1,font="arial 12 bold",width=5)
rb1.place(x=270,y=350)
rb2=Radiobutton(root,text="Female",variable=n1,relief='groove',bd=5,value=2,font="arial 12 bold",width=5)
rb2.place(x=358,y=350)
l9=Label(root,text="Email",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l9.place(x=10,y=400)
def validateemail(event):
    email=e9.get()
    pattern="^[A-Za-z][A-Za-z0-9]*[@][A-Za-z]{5}[.][a-zA-z]{3}$"
    res=re.findall(pattern,email)
    if(not res):
        mb.showwarning("Warning","Not A Valid Email")
        e9.delete(0,'end')
        
e9=Entry(root,width=25,bg="pink",bd=10,relief='groove')
e9.place(x=270,y=400)
e9.bind('<FocusOut>',validateemail)


l10=Label(root,text="Address",bg="sky blue",fg="black",font="arial 15 bold",relief='groove',bd=5,width=15)
l10.place(x=10,y=460)
ta=Text(root,height=5,width=20)
ta.place(x=270,y=450)
bt=Button(root,text="Submit",bg="pink",fg="green",font="arial 20 bold",relief='groove',bd=10,width=10,command=new_student)
bt.place(x=240,y=570)
def directory():
    global filename
    filename=fd.askopenfilename()
   
bt2=Button(root,text="Upload-Image",bg="sky blue",fg="black",font="arial 15 bold",command=directory,relief='groove',bd=5,width=15)
bt2.place(x=10,y=520)


def home():
 root.destroy()
 runpy.run_module('main_page')

bt4=Button(root,text="<--HOME",bg="pink",fg="green",font="arial 12 bold",relief="groove",bd=8,command=home,width=10)
bt4.place(x=5,y=600)

root.mainloop()
    


