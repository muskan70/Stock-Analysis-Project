import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *

class prediction: 
    def __init__(self,data):
        self.data=data
        self.predictfunction()
        
    def predictfunction(self):
        dataset=self.data[['Open','Close','High','Low']]
        dataset['H-L'] = dataset['High'] - dataset['Low']
        dataset['O-C'] = dataset['Close'] - dataset['Open']
        dataset['3day MA'] = dataset['Close'].shift(1).rolling(window = 3).mean()
        dataset['10day MA'] = dataset['Close'].shift(1).rolling(window = 10).mean()
        dataset['30day MA'] = dataset['Close'].shift(1).rolling(window = 30).mean()
        dataset['Std_dev']= dataset['Close'].rolling(5).std()
        dataset['daily_returns']=(dataset['Close']/dataset['Close'].shift(1))-1
        dataset['Price_Rise'] = dataset['Close'].shift(-1) - dataset['Close']
        dataset=dataset.dropna()

        X = dataset.iloc[:, 4:-1]
        y = dataset.iloc[:, -1]
        split = int(len(dataset)*0.8)
        X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]

        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        from sklearn import linear_model
        clf=linear_model.LinearRegression()
        clf.fit(X_train,y_train)
        y_pred=clf.predict(X_test)

        dataset['y_pred'] = np.NaN
        dataset.iloc[(len(dataset) - len(y_pred)):,-1] = y_pred
        dataset = dataset.dropna()

        import matplotlib.pyplot as plt
        plt.figure(figsize=(10,5))
        plt.scatter(dataset.index,dataset['Price_Rise'],color='r',label='Market returns')
        plt.plot(dataset['y_pred'], color='g', label='Strategy Returns',linewidth=3)
        plt.legend()
        plt.show()