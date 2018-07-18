import tkinter as tk
from tkinter import *
import pandas as pd
from stockextraction import analysis

class stockwindow:
    def __init__(self,type):
        stocklist=tk.Tk()
        self.master=stocklist
        self.type=type
        if(self.type==1):
            self.filename='NSEcodes.xlsx'
        elif(self.type==2):
            self.filename='BSEcodes.xlsx'
        stocklist.title("List of Stocks")
        stocklist.geometry("300x200")
        l=Label(self.master,text="Name of Stocks")
        l.pack(fill=BOTH)
        data=self.extractstocks()
        self.createbutton(data)
        stocklist.mainloop()
        
    def extractstocks(self):
        data=pd.read_excel(self.filename)
        return data['Codes']
    
    def createbutton(self,data):
        scrollbar = Scrollbar(self.master)
        scrollbar.pack( side = RIGHT, fill = BOTH )
        
        def onselect(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            if(self.type==1):
                s=analysis("NSE",value)
            else:
                s=analysis("BSE",value)
            

        mylist = Listbox(self.master, yscrollcommand = scrollbar.set )
        for i in data:
            s=i.split('/')[1]
            mylist.insert(END,s)
        mylist.pack(fill=BOTH)
        scrollbar.config( command = mylist.yview )   
        
        mylist.bind('<<ListboxSelect>>', onselect)
