from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer



class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")

        # I
        img1 = Image.open("AI01.png")
        img1 = img1.resize((500,200),Image.ANTIALIAS)  # Antialias is use to smoth sides of picture
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x=0,y=0,width=500,height=200)

        # II
        img2= Image.open("AI02.png")
        img2 = img2.resize((500,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root,image = self.photoimg2)
        f_lbl2.place(x=500,y=0,width=500,height=200)
        
        # III
        img3 = Image.open("AI03.png")
        img3 = img3.resize((500,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root,image = self.photoimg3)
        f_lbl3.place(x=1000,y=0,width=500,height=200)

        # Background Image
        img4 = Image.open("AI04.png")
        bg_img = img4.resize((1500,600),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root,image = self.photoimg4)
        bg_lbl.place(x=0,y=200,width=1510,height=600)

        title_lbl = Label(bg_lbl,text = "FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20,"bold"),bg="white",fg="red",)
        title_lbl.place(x=0,y=0,width=1500,height=50)
        title_lbl.pack()

        #Student button
        img5 = Image.open("AI05.png")
        img5 = img5.resize((300,140),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_lbl,image=self.photoimg5,command = self.student_details,cursor="hand2",fg="white",bg="darkblue") # here we using command 
        b1.place(x=100,y=100,width=300,height=140)

        b1 = Button(bg_lbl,text="STUDENT",command = self.student_details,cursor="hand2",fg="white",bg="darkblue")
        b1.place(x=100,y=240,width=300,height=20)

        #Detect Face Button
        img6 = Image.open("AI06.png")
        img6 = img6.resize((300,140),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_lbl,image=self.photoimg6,cursor="hand2",command=self.face_data,fg="white",bg="darkblue")
        b1.place(x=500,y=100,width=300,height=140)

        b1 = Button(bg_lbl,text="Face Detector",cursor="hand2",command=self.face_data,fg="white",bg="darkblue")
        b1.place(x=500,y=240,width=300,height=20)

        #Attendence button
        img7 = Image.open("AI07.png")
        img7 = img7.resize((300,140),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_lbl,image=self.photoimg7,cursor="hand2",command=self.Attendance_data,fg="white",bg="darkblue")
        b1.place(x=900,y=100,width=300,height=140)

        b1 = Button(bg_lbl,text="Attendence",cursor="hand2",command=self.Attendance_data,fg="white",bg="darkblue")
        b1.place(x=900,y=240,width=300,height=20)

        #Train Data button
        img8 = Image.open("AI08.png")
        img8 = img8.resize((300,140),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.train_data,fg="white",bg="darkblue")
        b1.place(x=100,y=300,width=300,height=140)

        b1 = Button(bg_lbl,text="Train Data",cursor="hand2",command=self.train_data,fg="white",bg="darkblue")
        b1.place(x=100,y=440,width=300,height=20)

        #Photoes
        img9 = Image.open("AI09.png")
        img9 = img9.resize((300,140),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img,fg="white",bg="darkblue")
        b1.place(x=500,y=300,width=300,height=140)

        b1 = Button(bg_lbl,text="Photos",cursor="hand2",command=self.open_img,fg="white",bg="darkblue")
        b1.place(x=500,y=440,width=300,height=20)


        #Developer
        img10 = Image.open("AI10.png")
        img10 = img9.resize((300,140),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_lbl,image=self.photoimg10,command = self.dev,cursor="hand2",fg="white",bg="darkblue")
        b1.place(x=900,y=300,width=300,height=140)

        b1 = Button(bg_lbl,text="Developer",command = self.dev,cursor="hand2",fg="white",bg="darkblue")
        b1.place(x=900,y=440,width=300,height=20)



    def open_img(self):
        os.startfile("data")

    # Function 
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def dev(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

