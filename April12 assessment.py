# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:45:23 2018

@author: user
"""
import pandas as pd
import numpy as np

data  = {'name': ['Henry','Susane','Tom','Fer','Yack'],
        'age': [54,27,46,38,12],
        'gender': ['Male','Female','Male','Male','Male'],
        'height': [17,23,12,15,32],
         'weight': [112,50,75,64,37],
         'BMI': [0,0,0,0,0],
         'Status':[' ',' ',' ',' ',' ']}

data1  = {'BMI': []}
dt = pd.DataFrame(data ,)
dt1=pd.DataFrame(data1 ,)
print (dt)

print(dt.sort_values(by=['height'], ascending=[False]))

name=dt['name'].values
height=dt['height'].values
weight=dt['weight'].values
e=[]
s=[]


i=0



while i<5:
   
    bmi = weight[i]/(height[i]*height[i])
    e.append(bmi)  
    if bmi <= 18.5:
        s.append('Underweight')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'You are underweight.')

    elif bmi > 18.5 and bmi < 25:
        s.append('Normal')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'You are normal.')

    elif bmi > 25 and bmi < 30:
        s.append('Overweight')
        print("for name of %s" %name[i])
        print('your BMI is', bmi,'You are overweight.')

    elif bmi > 30:
        s.append('Obese')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'You are obese.')

    
    i=i+1


se = pd.Series(e)
dt['BMI'] = se.values

se1 = pd.Series(s)
dt['Status'] = se1.values

dt.groupby(['Status'])

print(dt)
