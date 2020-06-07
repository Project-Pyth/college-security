import face_recognition
import cv2
import numpy as np
import mysql.connector
import tkinter.messagebox as mb
from tkinter import *


db=mysql.connector.connect(host="localhost",user="root",password="evneet1234",database="evneet")
cursor=db.cursor()
cursor.execute("select * from student_info")
rows=cursor.fetchall()   

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

known_face_encodings=[]
known_face_names=[]
rollno=[]
rno=0



# Load a sample picture and learn how to recognize it.
for row in rows:
    obama_image = face_recognition.load_image_file(row[10])
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings.append(obama_face_encoding)
    
    known_face_names.append(row[0].split()[0])
    rollno.append(row[9])
    
    
#db.close()

if len(known_face_encodings)!=0 and len(known_face_names)!=0:
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
          # Grab a single frame of video
          ret, frame = video_capture.read()

          # Resize frame of video to 1/4 size for faster face recognition processing
          small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

          # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
          rgb_small_frame = small_frame[:, :, ::-1]

          # Only process every other frame of video to save time
          if process_this_frame:
               # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
                    name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                       name = known_face_names[best_match_index]
                       rno=rollno[best_match_index]
    
                    face_names.append(name)

          process_this_frame = not process_this_frame


    # Display the results
          for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

        # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
          cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
          if cv2.waitKey(1) & 0xFF == ord('q'):
              print(face_names)
            
              if "Unknown" not in face_names:
                 #mb.showinfo("Info","Student Found in Record")
                 print(rno)
                 top=Toplevel()
                 top.geometry("650x650+700+100")
                 top.resizable(False,False)
                 top.config(background="black")
                 
          
                 head=Label(top,text="WELCOME TO P.M.N COLLEGE",width=35,font=30,bg="sky blue",fg="navy blue",bd=10,relief="groove")
                 head.place(x=130,y=10)
                 
                 cursor.execute("select * from  student_info where roll_no=%d"%(rno))
                 t2=cursor.fetchone()

                 p=PhotoImage(file=t2[10])
                 l=Label(top,image=p)
                 l.place(x=380,y=100,width=265,height=300)
                 
                 l1=Label(top,text="Name",bd=10,relief="groove",bg="black",fg="red",font=20,width=15)
                 l1.place(x=10,y=80)
                 
                 l2=Label(top,text=t2[0],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
                 l2.place(x=200,y=80)
                 l3=Label(top,text="Roll-No",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
                 l3.place(x=10,y=150)
                 l10=Label(top,text=rno,width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
                 l10.place(x=200,y=150)
                 
                 l4=Label(top,text="Course",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
                 l4.place(x=10,y=220)
                 l5=Label(top,text=t2[1],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
                 l5.place(x=200,y=220)
                 l6=Label(top,text="Father-Name",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
                 l6.place(x=10,y=290)
                 l7=Label(top,text=t2[4],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
                 l7.place(x=200,y=290)
                 l8=Label(top,text="Mother-Name",width=15,bd=10,relief="groove",bg="black",fg="red",font=20)
                 l8.place(x=10,y=360)
                 l9=Label(top,text=t2[5],width=15,bd=10,relief="groove",bg="black",fg="green",font=20)
                 l9.place(x=200,y=360)
                 l12=Label(top,text=t2[0],bd=10,relief="groove",bg="black",fg="red",font=20,width=15)
                 l12.place(x=450,y=410)
                 
              else: 
                 mb.showinfo("Warning","Student Not Found in Record") 
              break
else:
    mb.showwarning("Warning","No Record Found in Database")
    
db.close()    
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#mainloop()
