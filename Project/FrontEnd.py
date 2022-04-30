class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Curve Meter")

        self.enterGrade_label = Label(master, text = "Enter the Grade",
        foreground = "lime", background= "black", width=20, height=10)
        self.enterGrade_label.pack()

        self.entry = Entry(master, text= "test entry", fg = "lime", bg="black", width=24,)
        self.entry.pack()
    
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
import math
from scipy import stats
import matplotlib.pyplot as plt

from Backend import *

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