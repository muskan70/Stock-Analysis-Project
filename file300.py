import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
import quandl
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



class histogram_of_dailyreturns:
    def __init__(self,sname,data):
        self.sname=sname
        self.data=data
        root=tk.Tk()
        self.master=root
        root.title("graph of Stock")
        root.geometry("500x600")
        self.plotgraph()
        root.mainloop()
    
    def plotgraph1(self,a):
        dr=(self.data/self.data.shift(1))-1
        dr[0]=0
        mean=dr.mean()
        std=dr.std()
        a.hist(dr,bins=50)
        a.axvline(mean,color='w',linestyle='dashed')
        a.axvline(std,color='w',linestyle='dashed')
        a.axvline(-std,color='w',linestyle='dashed')
        a.set_title(self.sname)    
   
    def plotgraph(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        self.plotgraph1(a)
        canvas = FigureCanvasTkAgg(f, self.master)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self.master)
        toolbar.update()
        canvas._tkcanvas.pack(fill=BOTH)
