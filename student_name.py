# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:18:19 2022

@author: Yogita Hemant Patil
"""
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from glob import glob
from tkinter import messagebox
from subprocess import call
#from tkcalendar import Calendar
from datetime import date

class Students_name:
    def __init__(self):
        self.students_name = []
        
    def names(self):
        self.my_list = os.listdir(path="images")
        for per in self.my_list:
            self.students_name.append(os.path.splitext(per)[0])
        print(self.students_name)
        return self.students_name,self.my_list