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

        self.varOne = IntVar(master)
        self.check_button = tk.Checkbutton(master, text="sqrtCurver", variable=self.varOne)
        self.check_button.pack()

        self.varTwo = IntVar(master)
        self.check2_button = tk.Checkbutton(master, text="linearCurver", variable=self.varTwo)
        self.check2_button.pack()

        self.varThree = IntVar(master)
        self.check3_button = tk.Checkbutton(master, text="GuzmanCurver", variable=self.varThree)
        self.check3_button.pack()

        self.varFour = IntVar(master)
        self.check4_button = tk.Checkbutton(master, text="normalCurver", variable=self.varFour)
        self.check4_button.pack()

        self.button = tk.Button(master, text='Run', command=self.RunAction)
        self.button.pack()

        self.filename = ''

    
    def UploadAction(self):
        self.filename = filedialog.askopenfilename()

    def RunAction(self):
        raw_df = pd.read_csv(self.filename)
        header = ['Name', 'Score']

        if self.varOne.get() == 1:
            curved_df = sqrtCurver(raw_df, 70)
            data = []

            for i in range(len(curved_df['Name'])):
                data.append([curved_df['Name'][i], curved_df['Score'][i]])

            with open('./sqrtCurve.csv', 'w', encoding='UTF8', newline='') as f:
                # create the csv writer
                writer = csv.writer(f)
                
                writer.writerow(header)
                writer.writerows(data)

        if self.varTwo.get() == 1:
            curved_df = linearCurver(raw_df, 100, 40)
            data = []

            for i in range(len(curved_df['Name'])):
                data.append([curved_df['Name'][i], curved_df['Score'][i]])

            with open('./linearCurve.csv', 'w', encoding='UTF8', newline='') as f:
                # create the csv writer
                writer = csv.writer(f)
                
                writer.writerow(header)
                writer.writerows(data)

        if self.varThree.get() == 1:
            curved_df = GuzmanCurver(raw_df, 90)
            data = []

            for i in range(len(curved_df['Name'])):
                data.append([curved_df['Name'][i], curved_df['Score'][i]])

            with open('./guzmanCurve.csv', 'w', encoding='UTF8', newline='') as f:
                # create the csv writer
                writer = csv.writer(f)
                
                writer.writerow(header)
                writer.writerows(data)

        if self.normalCurver.get() == 1:
            curved_df = sqrtCurver(raw_df, 90)
            data = []

            for i in range(len(curved_df['Name'])):
                data.append([curved_df['Name'][i], curved_df['Score'][i]])

            with open('./normalCurve.csv', 'w', encoding='UTF8', newline='') as f:
                # create the csv writer
                writer = csv.writer(f)
                
                writer.writerow(header)
                writer.writerows(data)


    
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
