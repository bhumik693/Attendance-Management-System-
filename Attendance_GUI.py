9#!/usr/bin/env python
# coding: utf-8

# In[35]:


from tkinter import *
from PIL import Image,ImageTk
import os
from subprocess import call
import statistics_final as st
import untitled0_final as uf

#take attendance
#register a student
#remove student
#get attendance data

class home_page:
    def __init__(self,main_root):
        self.main_root = main_root
        self.main_root.title("STUDENT MANAGEMENT SYSTEM")
        self.main_root.geometry("1000x500")
        self.main_root.minsize(1000,500)
        self.main_root.maxsize(1000,500)
        self.gui()
    
    def statistics_file(self):
        self.main_root.destroy()
        attend = Tk()
        obj = st.stats(attend)
        attend.mainloop()
        # self.path = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT"
        # os.chdir(self.path)
        # call(["python","statistics_final.py"])
        
    def image_register_file(self):
        self.main_root.destroy()
        self.path = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT"
        os.chdir(self.path)
        call(["python","image_register_final.py"])
        
    def login_file(self):
        self.main_root.destroy()
        self.path = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT"
        os.chdir(self.path)
        call(["python","login_page.py"])
        
    def attendance(self):
        #self.main_root.destroy()
        self.path = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT"
        self.obj = uf.Encoding_Attendance(self.datevar.get())
        
        # os.chdir(self.path)
        # call(["python","untitled0_final.py"])

    def gui(self):
        self.image1 = Image.open(r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT\Login.png") 
        self.image1 = self.image1.resize((400, 500))
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(image = self.photoimage1, borderwidth = 6, relief = RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)

        self.main_frame = Frame(self.main_root, width=600, height=500, relief=SUNKEN, bg='#3a86ff')
        self.main_frame.place(x=0, y = 0)

        self.main = Label(self.main_root, text="STUDENT MANAGEMENT SYSTEM", font="comicsans 20 bold", bg='red', 
                     fg='white', width=35, height=1)
        self.main.place(x = 0, y = 50)

        self.attendance_button = Button(self.main_root, text="Take Attendance", font="comicsans 13 bold", bg='green', 
                                   fg='white', width=17, height=1,command = self.attendance)
        self.attendance_button.place(x=200, y=150)
        
        self.datevar = StringVar()
        
        self.date_required = Entry(self.main_root,textvariable=self.datevar,width=20)
        self.date_required.place(x=400 ,y = 150)

        self.register_button = Button(self.main_root, text="Register a Student", font="comicsans 13 bold", bg='green', 
                                 fg='white', width=17, height=1,command=self.image_register_file)
        self.register_button.place(x=200, y=225)

        # self.remove_button = Button(self.main_root, text="Remove Student", font="comicsans 13 bold", bg='green',
        #                        fg='white', width=17, height=1)
        # self.remove_button.place(x=200, y=300)

        self.getdata_button = Button(self.main_root, text="Get Attendance Data", font="comicsans 13 bold", bg='green', 
                                fg='white', width=17, height=1,command=self.statistics_file)
        self.getdata_button.place(x=200, y=300)

        self.logout_button = Button(self.main_root, text="Log Out", font="comicsans 10 bold", bg='green', 
                               fg='white', width=17, height=1,command=self.login_file)
        self.logout_button.place(x=425, y=100)
        
    


# if __name__ == '__main__':
#     main_root=Tk()
#     obj = home_page(main_root)

#     main_root.mainloop()


# In[ ]:




