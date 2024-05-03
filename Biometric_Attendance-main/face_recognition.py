from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector   
import cv2
import os   # open cv is a open source compatitor vision liberary where more than 1000 algo available  
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text = "FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green",)
        title_lbl.place(x=0,y=0,width=1550,height=50)

        img_top = Image.open("AI20.png")
        img_top = img_top.resize((1550,750),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root,image = self.photoimg_top)
        f_lbl_top.place(x=0,y=50,width=1550,height=750)

        rec_btn = Button(f_lbl_top,text="Face Recognition",command=self.face_recog,font=("times new roman",30,"bold"),bg = "darkgreen",fg ="white",width=200)
        rec_btn.place(x =993,y=655,width=300,height=50)



    #   Attendence
    def mark_attendence(self,i,r,n,b):
        with open("rob.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((','))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (b not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{b},{dtString},{d1},present")
                




        # Face Recognition
    
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer")       
                my_cursor1 = conn.cursor() 
                
                my_cursor1.execute("SELECT name FROM face_recognizer.student where id="+str(id)) 
                n = my_cursor1.fetchone()
                n = "+".join(n) 

                my_cursor1.execute("SELECT Roll_No FROM face_recognizer.student where id="+str(id))
                r = my_cursor1.fetchone()
                r = "+".join(r)

                my_cursor1.execute("SELECT Branch FROM face_recognizer.student where id="+str(id))
                b = my_cursor1.fetchone()
                b = "+".join(b) 

                my_cursor1.execute("SELECT id FROM face_recognizer.student where id="+str(id))
                i = my_cursor1.fetchone()
                i = "+".join(i) 

                if confidence>77:  # this function is used to print name, roll_number etc when it recognize face
                    cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Branch:{b}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    self.mark_attendence(i,r,n,b)
                    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]
                
                
            return coord
            
        def recognize(img,clf,faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
            
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # here 0 is write because we using our laptop camera for other we use 1
        i = 0    
        while True:
            i += 1
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()











if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()