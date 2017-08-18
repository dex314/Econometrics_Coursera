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

#%% 
## EXERCISE 1.1
dirc = 'C:\\Users\\SchillW\\OneDrive - FNBCorp\\Econ_Coursera\\Wk1\\'

f = 'TrainExer11.xls'

df = pd.read_excel(dirc + f)

## histograms
plt.figure()
h1 = df['Expenditures'].plot.hist()
plt.title('Expenditures')
plt.figure()
h2 = df['Age'].plot.hist()
plt.title('Age')

s1 = df.plot.scatter(y='Expenditures',x='Age')

##b - alot of high expenditures, alot of 35 year olds. points dont associate with straight line
## appear to be two groups of points in the scatter plot based on age
##c - seems sensible to seprate the dat into two age groups 

means = np.mean(df,axis=0)
print means

gt40 = df['Age']>=40
lt40 = df['Age']<40
exp_gte40 = np.mean(df['Expenditures'][gt40])
exp_lt40 = np.mean(df['Expenditures'][lt40])

##f  50-> >= 40 therfor expenditures would be 95.8 for prediction

#%%
## EXERCISE 1.2
'''
log(y_i) = a+B*log(x_i) + eps_i 

exp(...)

y_i = exp( a + eps_i )*x_i^B
dy/dx = B*(exp(a+epsi)*x^(B-1)) = B/xi * exp(a+eps_i)*x^B = B*yi/xi
and dy/dx * xi/yi = B*yi/xi * xi/yi = B

dy/dx = B * 1/x_i
elasticity: dy/dx*xi/yi = B/xi*xi/yi = B/yi
'''
#%%
## Exercise 1.3



#%%
## TEST 1
dirc = 'C:\\Users\\SchillW\\OneDrive - FNBCorp\\Econ_Coursera\\Wk1\\'
f = 'TestExer1-sales-round1.xls'
df = pd.read_excel(dirc + f)

df.plot.scatter(y='Sales',x='Advertising')
## If we were to try and fit a regression line through this data we would see that it
## was significantly skewed to a negative slope because of the outliar point of 50 sales.

## C - the residuals are mostly close together with the exception of the one related to the outliar with the 
## predicition falling significantly short

xwk1 = np.reshape(df['Advertising'],(len(df),1))
ywk1 = np.reshape(df['Sales'],(len(df),1))

import statsmodels.api as sm
xwk1i = sm.add_constant(xwk1)
mod2 = sm.OLS(ywk1,xwk1i)
res = mod2.fit()
print res.summary()

yhat_wk1 = np.reshape(xwk1i.dot(res.params), (len(ywk1),1))
resids = pd.DataFrame( (ywk1-yhat_wk1) )
resids.plot.hist(['g']), title('Histogram of Residuals')


## D - possibly by replacing the outliar with the median or mean of the data in that variable

ywk1a = np.copy(ywk1)
ystd = np.std(ywk1a)
devs_out = (2*ystd+np.mean(ywk1a))
ywk1a[ywk1a > devs_out] = np.median(ywk1)

mod_a = sm.OLS(ywk1a,xwk1i)
res_a = mod_a.fit()
print res_a.summary()
















