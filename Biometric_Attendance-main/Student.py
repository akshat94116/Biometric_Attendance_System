from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector   
import cv2   # open cv is a open source compatitor vision liberary where more than 1000 algo available  

class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")


        # Variables
        self.var_branch = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_std_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_sem = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_sec = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()

        # I
        img1 = Image.open("AI11.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)  # Antialias is use to smoth sides of picture
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x=0,y=0,width=500,height=130)

        # II
        img2= Image.open("AI12.png")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root,image = self.photoimg2)
        f_lbl2.place(x=500,y=0,width=500,height=130)
        
        # III
        img3 = Image.open("AI13.png")
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root,image = self.photoimg3)
        f_lbl3.place(x=1000,y=0,width=500,height=130)


        # Background Image
        img4 = Image.open("AI04.png")
        bg_img = img4.resize((1500,600),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root,image = self.photoimg4)
        bg_lbl.place(x=0,y=130,width=1510,height=730)

        title_lbl = Label(bg_lbl,text = "STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen",)
        title_lbl.place(x=0,y=0,width=1500,height=50)

        main_frame1 = Frame(bg_lbl,bd=2)
        main_frame1.place(x=20,y=57,width=1465,height=700)

        #left label frame
        left_frame = LabelFrame(main_frame1,bd=2,text="Student Details",font=("times new roman",14,"bold"))
        left_frame.place(x=20,y=10,width=700,height=585)

        img_left = Image.open("AI14.png")
        img_left = img_left.resize((695,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(left_frame,image = self.photoimg_left)
        f_lbl_left.place(x=0,y=0,width=695,height=100)

        #Current course
        current_course_frame = LabelFrame(left_frame,bd=2,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=0,y=100,width=695,height=125)

        course_lebel = Label(current_course_frame,text="Course",font=("times new roman",14,"bold"))
        course_lebel.grid(row=0,column=0)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width = 15,state="readonly")
        course_combo["values"] = ("Select Course","B.tech","MBA","B.Pharma","D.Pharma")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=10,pady=10)
        branch_lebel = Label(current_course_frame,text="Branch",font=("times new roman",14,"bold"))
        branch_lebel.grid(row=1,column=0)

        branch_combo = ttk.Combobox(current_course_frame,textvariable=self.var_branch,font=("times new roman",14,"bold"),width = 15,state="readonly")
        branch_combo["values"] = ("Select Department","CSE","CSDS","AI","IT")
        branch_combo.current(0)
        branch_combo.grid(row=1,column=1,padx=10,pady=10)

        year_lebel = Label(current_course_frame,text="Year",font=("times new roman",14,"bold"))
        year_lebel.grid(row=0,column=2)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),width = 15,state="readonly")
        year_combo["values"] = ("Select Batch","2022-23","2021-22","2020-21","2019-20")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=10,pady=10)


        sem_lebel = Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"))
        sem_lebel.grid(row=1,column=2)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",15,"bold"),width = 15,state="readonly")

        sem_combo["values"] = ("Select Semester","","I","II","III","IV","V","VI","VII","VII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10)


        # class student information
        class_student_frame = LabelFrame(left_frame,bd=2,text="Class Student Information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=0,y=230,width=695,height=325)

        studentid_label = Label(class_student_frame,text="Student ID:",font=("times new roman",15,"bold"))
        studentid_label.grid(row=0,column=0)

        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        studentid_entry.grid(row=0,column=1,padx = 5,pady = 5)

        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",15,"bold"))
        student_name_label.grid(row=0,column=3)

        student_name_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_stu_name,font=("times new roman",15,"bold")) # ttk is used for style
        student_name_entry.grid(row=0,column=4,padx = 5,pady = 5)

        class_section_label = Label(class_student_frame,text="Class Section:",font=("times new roman",15,"bold"))
        class_section_label.grid(row=1,column=0)

        class_section_entry = ttk.Entry(class_student_frame,textvariable = self.var_sec,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        class_section_entry.grid(row=1,column=1,padx = 5,pady = 5)

        roll_no_label = Label(class_student_frame,text="Roll No:",font=("times new roman",15,"bold"))
        roll_no_label.grid(row=1,column=3)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        roll_no_entry.grid(row=1,column=4,padx = 5,pady = 5)



        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",15,"bold"))
        gender_label.grid(row=2,column=0)

        gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        gender_entry.grid(row=2,column=1,padx = 5,pady = 5)

        DOB_label = Label(class_student_frame,text="DOB:",font=("times new roman",15,"bold"))
        DOB_label.grid(row=2,column=3)

        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        DOB_entry.grid(row=2,column=4,padx = 5,pady = 5)


        Email_label = Label(class_student_frame,text="Email ID:",font=("times new roman",15,"bold"))
        Email_label.grid(row=3,column=0)

        Email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        Email_entry.grid(row=3,column=1,padx = 5,pady = 5)

        phone_no_label = Label(class_student_frame,text="Phone No:",font=("times new roman",15,"bold"))
        phone_no_label.grid(row=3,column=3)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        phone_no_entry.grid(row=3,column=4,padx = 5,pady = 5)


        Address_label = Label(class_student_frame,text="Address:",font=("times new roman",15,"bold"))
        Address_label.grid(row=4,column=0)

        Address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",15,"bold")) # ttk is used for style
        Address_entry.grid(row=4,column=1,padx = 5,pady = 5)

        teacher_name_label = Label(class_student_frame,text="Teacher Name:",font=("times new roman",14,"bold"))
        teacher_name_label.grid(row=4,column=3)

        teacher_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",14,"bold")) # ttk is used for style
        teacher_name_entry.grid(row=4,column=4,padx = 5,pady = 5)

        #radio Buttons
        radiobt1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobt1.grid(row = 5,column =0)

        radiobt2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobt2.grid(row = 5,column =1)

        # Button Frame

        button_frame = LabelFrame(class_student_frame,bd=2,relief = RIDGE)  # here relief is use for certain 
        button_frame.place(x=0,y=215,width=700,height=80)                   #simulated 3-D effects around the outside of the widget

        save_btn = Button(button_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn = Button(button_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        reset_btn.grid(row=0,column=3)

        takephotesample_btn = Button(button_frame,text="TakePhotoSample",command = self.generate_dataset,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=35)
        takephotesample_btn.place(x=0,y=35)

        updatephotosample_btn = Button(button_frame,text="UpdatePhotoSample",font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=35)
        updatephotosample_btn.place(x=350,y=35)

                                                                                                    



        #Right label frame
        right_frame = LabelFrame(main_frame1,bd=2,text="Student Details",font=("times new roman",14,"bold"))
        right_frame.place(x=730,y=10,width=700,height=585)

        img_right = Image.open("AI15.png")
        img_right = img_right.resize((695,100),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = Label(right_frame,image = self.photoimg_right)
        f_lbl_right.place(x=0,y=0,width=695,height=100)

        # Search System
        search_frame = LabelFrame(right_frame,bd=2,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=0,y=100,width=695,height=70)

        search_label = Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width = 17,state="readonly")

        search_combo["values"] = ("Select","Roll_No","Student_id","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=8,pady=8)

        search_btn = Button(search_frame,text="Search",font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        search_btn.grid(row=0,column=2,padx=10)

        showall_btn = Button(search_frame,text="Show All Data",font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=17)
        showall_btn.grid(row=0,column=3)


        # Table frame
        table_frame = Frame(right_frame,bd=2,bg = "white",relief=RIDGE)
        table_frame.place(x=0,y=175,width=695,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=("Course","Branch","Year","Semester","id","Name","Roll_No","Gender","DOB","Email_id","Phone_No","Address","Teacher_Name","Section","Photo_Sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("Name",text="Student Name")
    
        self.student_table.heading("Roll_No",text="Roll_No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email_id",text="Email_id")
        self.student_table.heading("Phone_No",text="Phone-No.")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher_Name",text="Teacher_Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Photo_Sample",text="Photo_Sample")

        self.student_table.column("Course",width=100)
        self.student_table.column("Branch",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll_No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email_id",width=100)
        self.student_table.column("Phone_No",width=100)
        self.student_table.column("Address",width=200)
        self.student_table.column("Teacher_Name",width=100)
        self.student_table.column("Section",width=50)
        self.student_table.column("Photo_Sample",width=100)

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # Function for add data 
    def add_data(self):
        if self.var_branch.get()=="Select Branch" or self.var_stu_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All Field are required",parent = self.root)#  here we using parent to show error msg to show in student page
        else:
            try: 
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer")       
                my_cursor = conn.cursor() 
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_course.get(),
                    self.var_branch.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_stu_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_sec.get(),
                    self.var_radio1.get()
                                    )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent = self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)


    # Fetch data function 
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer") 
        my_cursor = conn.cursor()  
        my_cursor.execute("Select * from student")
        data  = my_cursor.fetchall()    

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values = i) 
            conn.commit()
        conn.close()  


# Get Cursor
    def get_cursor(self,event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_branch.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_sec.set(data[13]),
        self.var_radio1.set(data[14])



#    Update function
    def update_data(self):
        if self.var_branch.get()=="Select Branch" or self.var_stu_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All Field are required",parent = self.root)
        else:
            try:
                upadate = messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)
                if upadate>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer")       
                    my_cursor = conn.cursor() 
                    my_cursor.execute("update student set Course=%s,Branch=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,DOB=%s,Email_id=%s,Phone_No=%s,Address=%s,Teacher_Name=%s,Section=%s,Photo_Sample=%s where id=%s",(
                    self.var_course.get(),
                    self.var_branch.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_sec.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)



    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error","Student ID must be required",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer") 
                    my_cursor = conn.cursor()
                    sql = "delete from student where Roll_No = %s"
                    val = (self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete',"Successfully deleted student details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)



    # Define reset function 
    def reset_data(self):
        self.var_course.set("Select Department"),
        self.var_branch.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_stu_name.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_sec.set(""),
        self.var_radio1.set("")



    # Generate data set or take photo samples
    def generate_dataset(self):
        if self.var_branch.get()=="Select Branch" or self.var_stu_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","All Field are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Rav@1234",database = "face_recognizer")       
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1 
                my_cursor.execute("update student set Course=%s, Branch=%s, Year=%s, Semester=%s, Name=%s,Roll_No=%s, Gender=%s, DOB=%s, Email_id=%s, Phone_No=%s, Address=%s, Teacher_Name=%s, Section=%s, Photo_Sample=%s where id=%s",(
                    self.var_course.get(),
                    self.var_branch.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_sec.get(),
                    self.var_radio1.get(),
                     self.var_std_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
        # Load predefined data on face fromtals from open cv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5) # 1.3 = scaling factor,5 = minimum neighbor
                    
                    #<>>return  1
                    for (x, y, w, h) in faces:
                        #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        face_cropped = img[y:y + h, x:x + w] 
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret,myframe = cap.read()
                    #if face_cropped(myframe) is not None:
                    img_id += 1
                     #   face = cv2.resize(face_cropped(myframe),(450,450))
                    face = cv2.cvtColor(myframe,cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root) 



if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()