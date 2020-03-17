#!/usr/bin/env python
# coding: utf-8

# In[76]:


#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[123]:


#Declaring variables

x=[1,2,3]
y=[1,2,3]
x=np.array(x)
y=np.array(y)
theta=np.zeros((2,))
theta[0]=0
theta[1]=0.5
m=x.shape[0]


# In[124]:


#Declaration of functions

def y_(theta,x):
    return theta[1]*x + theta[0]

def linear_regression(x,y):
    e=0
    y_hat = y_(theta,x)
    y_hat=np.array(y_hat)
    for i in range(m):
        e+=(y_hat[i] - y[i])**2
    #print(e)
    return(e/(2*m))

ans=linear_regression(x,y)
print(ans)


# In[125]:


#Visualization

plt.plot(x,y,color="green")
plt.show
plt.plot(x,y_hat,color="red")
plt.show


# In[ ]:




