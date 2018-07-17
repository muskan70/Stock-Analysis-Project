import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
import quandl
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



class analysis:
    def __init__(self,stype,sname):
        root=tk.Tk()
        self.master=root
        root.title("Analysis and Prediction")
        root.geometry("400x400")
        l=Label(self.master,text=sname).pack(fill=BOTH)
        url=stype+"/"+sname
        self.data=self.extractdata(url)
        self.printdetails()
        self.plotgraph()
        root.mainloop()
        
    def extractdata(self,name):
        quandl.ApiConfig.api_key = "jXPHrf-GmUoyAdmhjcxF"
        data = quandl.get(name)
        return data
        
    def printdetails(self):
        d=pd.DataFrame(self.data.tail(1).T)
        l=Label(self.master,text=d).pack()
     
    def plotgraph(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot(self.data['Open'])
        canvas = FigureCanvasTkAgg(f, self.master)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self.master)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
    