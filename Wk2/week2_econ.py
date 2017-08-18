# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 11:53:29 2016

@author: SchillW

Work for Econometrics course
"""

'''
Week 1
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

#%% 
## EXERCISE 2.1
dirc = 'C:\\Users\\SchillW\\Documents\\Econ_Coursera\\Wk2\\'

f = 'TrainExer21.xls'

df = pd.read_excel(dirc + f)

x = df['Female']
xc = sm.add_constant(x)

y = df['LogWage']

mod = sm.OLS(y,xc)
fit = mod.fit()
print fit.summary()

resid = y - (4.73-0.25*x)

rmod = sm.OLS(resid, sm.add_constant(df['Educ']))
rfit = rmod.fit()
print rfit.summary()

'''...'''
#%%

## WEEK2 HW

f2 = 'TrainExer25.xls'
df2 = pd.read_excel(dirc+f2)
y = df2['LogWage']
x1 = sm.add_constant(x) #from above
var = list(['Female','Age','Educ','Parttime'])
x2 = df2[var]

mod = sm.WLS(x1,x2)
fit = mod.fit()
print fit.summary()










