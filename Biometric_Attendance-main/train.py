from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector   
import cv2
import os   # open cv is a open source compatitor vision liberary where more than 1000 algo available  
import numpy as np



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red",)
        title_lbl.place(x=0,y=0,width=1550,height=50)

        img_top = Image.open("AI16.png")
        img_top = img_top.resize((515,300),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root,image = self.photoimg_top)
        f_lbl_top.place(x=0,y=50,width=515,height=300)

        img_left = Image.open("AI17.png")
        img_left = img_left.resize((515,300),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(self.root,image = self.photoimg_left)
        f_lbl_left.place(x=515,y=50,width=515,height=300)

        img_top3 = Image.open("AI18.png")
        img_top3 = img_top3.resize((515,300),Image.ANTIALIAS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)
        f_lbl_top3 = Label(self.root,image = self.photoimg_top3)
        f_lbl_top3.place(x=1030,y=50,width=515,height=300)


        img_bottom = Image.open("AI19.png")
        img_bottom = img_bottom.resize((1550,450),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(self.root,image = self.photoimg_bottom)
        f_lbl_bottom.place(x=0,y=400,width=1550,height=450)

        train_btn = Button(self.root,text="TRAIN DATA",command = self.train_classifier,font=("times new roman",30,"bold"),bg = "red",fg ="white",width=40)
        train_btn.place(x =0,y=350,width=1530,height=50)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")  # it convert image into gray scale
            imagenp = np.array(img,"uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==1300
        ida = np.array(ids)

        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ida)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!!",parent = self.root)
        






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()