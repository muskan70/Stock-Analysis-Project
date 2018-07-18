import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
import quandl
import matplotlib
from file50 import openvalues
from file98 import bollinger
from file150 import rollingmean 
from file200 import rollingstandard
from file249 import dailyreturns
from file300 import histogram_of_dailyreturns
from file347 import prediction
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



class analysis:
    def __init__(self,stype,sname):
        root=tk.Tk()
        self.master=root
        self.sname=sname
        self.value1="line graph of Open values"
        self.value2="For all"
        
        root.title("Analysis and Prediction")
        root.geometry("500x600")
        
        l=Label(self.master,text=sname)
        l.config(font=("Courier", 40))
        l.pack(fill=BOTH)
        
        l=Label(self.master,text="Current day Details")
        l.config(font=("Courier", 20))
        l.pack(fill=BOTH)
        url=stype+"/"+sname
        self.data=self.extractdata(url)
        self.printdetails()
        
        l=Label(self.master,text="Stock Statistics Description")
        l.config(font=("Courier", 20))
        l.pack(fill=BOTH)
        self.describedetails()
        
        l=Label(self.master,text="Stock Graph")
        l.config(font=("Courier", 20))
        l.pack(fill=BOTH)
        self.giveoptions()
        
        def predict():
            window=prediction(self.data)
        
        p=Button(self.master,text="Predicted Stock Returns",bg='yellow',command=predict)
        p.config(font=("Courier", 20))
        p.pack()
        root.mainloop()
        
    def extractdata(self,name):
        quandl.ApiConfig.api_key = "jXPHrf-GmUoyAdmhjcxF"
        data = quandl.get(name)
        start_date=data.index[0]
        end_date=data.index[-1]
        dates=pd.date_range(start_date,end_date)
        df=pd.DataFrame(index=dates)
        df=df.join(data)
        df.fillna(method="ffill",inplace=True)
        df.fillna(method="bfill",inplace=True)
        return df
        
    def printdetails(self):
        d=pd.DataFrame(self.data.tail(1).T)
        l=Label(self.master,text=d).pack()
        
    def describedetails(self):
        d=self.data['Open'].describe()
        l=Label(self.master,text=d).pack()    
        
    def giveoptions(self):
        Options1=["line graph of Open values","line graph of Daily Returns","histogram of Daily Returns",
                  "line graph of Rolling mean","line graph of Rolling standard","line graph of Bollinger bands"]
        Options2=["For all","For an year","For a month","For a week"]
        
        variable1 = StringVar(self.master)
        variable1.set(Options1[0])
        variable2 = StringVar(self.master)
        variable2.set(Options2[0])

        w1 = OptionMenu(self.master, variable1, *Options1)
        w1.config(width=25,bg='orange')
        w1.pack()
        w2 = OptionMenu(self.master, variable2, *Options2)
        w2.config(width=14,bg='orange')
        w2.pack()

        def ok():
            self.value1=variable1.get()
            self.value2=variable2.get()
            self.plotgraph()

        button = Button(self.master, text="Plot Graph", command=ok,bg='skyblue')
        button.pack()
        
    def setdata(self):
        data=self.data['Open']
        if(self.value2=="For all"):
            pass
        elif(self.value2=="For an year"):
            data=data.tail(365)
        elif(self.value2=="For a month"):
            data=data.tail(30)
        elif(self.value2=="For a week"):
            data=data.tail(7)
        return data
    
    def chooseplot(self,data):
        if(self.value1=="line graph of Open values"):
            window=openvalues(self.sname,data)
        elif(self.value1=="line graph of Daily Returns"):
            window=dailyreturns(self.sname,data)
        elif(self.value1=="histogram of Daily Returns"):
            window=histogram_of_dailyreturns(self.sname,data)
        elif(self.value1=="line graph of Bollinger bands"):
            window=bollinger(self.sname,data)
        elif(self.value1=="line graph of Rolling mean"):
            window=rollingmean(self.sname,data)
        elif(self.value1=="line graph of Rolling standard"):
            window=rollingstandard(self.sname,data)
        
        
    def plotgraph(self):
        data_for_graph=self.setdata()
        self.chooseplot(data_for_graph)