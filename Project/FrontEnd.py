from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
import math
from scipy import stats
import matplotlib.pyplot as plt
from tkinter import *
from Backend import *
import csv



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.test_button = Button(master, text = "Test Zoey", command = self.Zoey)
        self.test_button.pack()

    def greet(self):
        print("Greetings!")
    def Zoey(self):
        print("Hello from Zoey")

  
class UserInterface:
    
    def __init__(self, master):
        self.master = master
        master.title("Curve Meter")
        master.geometry("300x300")

        self.enterGrade_label = Label(master, text = "Open the csv file")
        self.enterGrade_label.pack()

       
        self.button = tk.Button(master, text='Open', command=self.UploadAction)
        self.button.pack()

        self.enterGrade_label = Label(master, text = "Select the type of curve")
        self.enterGrade_label.pack()


        self.check_button = Checkbutton(master, text="sqrtCurver")
        self.check_button.pack()

        self.check2_button = Checkbutton(master, text="linearCurver")
        self.check2_button.pack()

        self.check3_button = Checkbutton(master, text="GuzmanCurver")
        self.check3_button.pack()

        self.check4_button = Checkbutton(master, text="normalCurver")
        self.check4_button.pack()

    




 







    filename = ''
    def UploadAction(self):
        filename = filedialog.askopenfilename()

        df = pd.read_csv(filename)
        print('Selected:', type(filename))
        print(df)
    
    def sel():
        selection = "You selected the option"


  


root = tk.Tk()
my_gui = UserInterface(root)
root.mainloop()


'''
filename = ''

def UploadAction(event=None):
    filename = filedialog.askopenfilename()

    df = pd.read_csv(filename)
    print('Selected:', type(filename))
    print(df)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()
'''
