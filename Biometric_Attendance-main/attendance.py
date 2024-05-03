from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector   
import cv2   # open cv is a open source compatitor vision liberary where more than 1000 algo available  
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")

        # Variable
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_branch = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

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


        title_lbl = Label(self.root,text = "ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen",)
        title_lbl.place(x=0,y=130,width=1500,height=70)

        main_frame1 = Frame(bg_lbl,bd=2)
        main_frame1.place(x=20,y=75,width=1465,height=700)

        left_frame = LabelFrame(main_frame1,bd=2,text="Student Attendance Details",font=("times new roman",17,"bold"))
        left_frame.place(x=20,y=10,width=700,height=585)

        img_left = Image.open("AI14.png")
        img_left = img_left.resize((695,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(left_frame,image = self.photoimg_left)
        f_lbl_left.place(x=0,y=0,width=695,height=100)

        left_inside_frame1 = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame1.place(x=5,y=105,width=685,height=400)

        # Labels and entry

        attendanceid_label = Label(left_inside_frame1,text="Attendance ID:",font=("times new roman",15,"bold"))
        attendanceid_label.grid(row=0,column=0)

        attendanceid_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_id,font=("times new roman",15,"bold")) # ttk is used for style
        attendanceid_entry.grid(row=0,column=1,padx = 5,pady = 5)


        roll_label = Label(left_inside_frame1,text="Roll:",font=("times new roman",15,"bold"))
        roll_label.grid(row=0,column=2)

        roll_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_roll,font=("times new roman",15,"bold")) # ttk is used for style
        roll_entry.grid(row=0,column=3,padx = 5,pady = 5)

        Name_label = Label(left_inside_frame1,text="Name:",font=("times new roman",15,"bold"))
        Name_label.grid(row=1,column=0)

        Name_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_name,font=("times new roman",15,"bold")) # ttk is used for style
        Name_entry.grid(row=1,column=1,padx = 5,pady = 5)

        Branch_label = Label(left_inside_frame1,text="Branch:",font=("times new roman",15,"bold"))
        Branch_label.grid(row=1,column=2)

        Branch_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_branch,font=("times new roman",15,"bold")) # ttk is used for style
        Branch_entry.grid(row=1,column=3,padx = 5,pady = 5)

        Time_label = Label(left_inside_frame1,text="Time:",font=("times new roman",15,"bold"))
        Time_label.grid(row=2,column=0)

        Time_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_time,font=("times new roman",15,"bold")) # ttk is used for style
        Time_entry.grid(row=2,column=1,padx = 5,pady = 5)

        Date_label = Label(left_inside_frame1,text="Date:",font=("times new roman",15,"bold"))
        Date_label.grid(row=2,column=2)

        Date_entry = ttk.Entry(left_inside_frame1,width=20,textvariable=self.var_atten_date,font=("times new roman",15,"bold")) # ttk is used for style
        Date_entry.grid(row=2,column=3,padx = 5,pady = 5)

        attendance_status_label = Label(left_inside_frame1,text="Attendance Status:",font=("times new roman",15,"bold"))
        attendance_status_label.grid(row=3,column=0)

        self.attendance_status_combo = ttk.Combobox(left_inside_frame1,textvariable=self.var_atten_attendance,font=("times new roman",15,"bold"),width = 15,state="readonly")

        self.attendance_status_combo["values"] = ("Select Semester","Present","Absent")
        self.attendance_status_combo.current(0)
        self.attendance_status_combo.grid(row=3,column=1,padx=10,pady=10)



        #  Button Frame

        button_frame = LabelFrame(left_inside_frame1,bd=2,relief = RIDGE)  # here relief is use for certain 
        button_frame.place(x=5,y=250,width=675,height=80)                   #simulated 3-D effects around the outside of the widget

        save_btn = Button(button_frame,text="Import csv",command=self.import_csv,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=25)
        save_btn.grid(row=0,column=0)

        update_btn = Button(button_frame,text="Export",command=self.export_csv,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=22)
        update_btn.grid(row=0,column=1)


        reset_btn = Button(button_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg = "blue",fg ="white",width=22)
        reset_btn.grid(row=0,column=2)

    





        right_frame = LabelFrame(main_frame1,bd=2,text="Attendance Details",font=("times new roman",17,"bold"))
        right_frame.place(x=730,y=10,width=700,height=585)

        img_right = Image.open("AI15.png")
        img_right = img_right.resize((695,100),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = Label(right_frame,image = self.photoimg_right)
        f_lbl_right.place(x=0,y=0,width=695,height=100)


        table_frame = LabelFrame(right_frame,bd=2,relief = RIDGE)  # here relief is use for certain 
        table_frame.place(x=5,y=105,width=685,height=430)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","Roll_No","Name","Branch","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill = Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student Id")
        self.AttendanceReportTable.heading("Roll_No",text="Roll No")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Branch",text="Branch")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("Roll_No",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Branch",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


#### Fetch Data 


    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

#  import csv file function
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


# Export csv file function 
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" Successfully",parent = self.root)
        except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent = self.root)


    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_branch.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6]) 

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_branch.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()