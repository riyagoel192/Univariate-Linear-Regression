#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


#Declaration of variables

X=[1,2,3,4,5]
Y=[1,4,9,16,25]
X=np.array(X)
Y=np.array(Y)


# In[11]:


#defining functions

#starting with random theta values
def y_(theta,X):
    return theta[1]*X + theta[0]

def error(X,Y,theta):
    m=X.shape[0]                #m has value 5
    e= 0
    for i in range(m):
        y_hat = y_(theta,X[i])
        y= Y[i]
        e+= (y_hat - y)**2
    return e/m

def gradient(X,Y,theta):
    grad= np.zeros((2,))      #has 2 elements in array initialized with 0
    m= X.shape[0]
    for i in range(m):
        y_hat = y_(theta,X[i])
        y=Y[i]
        grad[0]+= (y_hat - y)
        grad[1]+= (y_hat - y)*X[i]
        
    return 2*grad/m

def gradient_descent(X,Y):
    theta=np.zeros((2,))
    lr = 0.01
    error_list =[]
    
    m= X.shape[0]
    for i in range(m):
        #compute error
        e = error(X,Y,theta)
        error_list.append(e)
        
        
        #update theta
        grad = gradient(X,Y,theta)
        theta[0]= theta[0] - lr*grad[0]
        theta[1]= theta[1] - lr*grad[1]
        
    return theta,error_list


# In[13]:


theta,error_list = gradient_descent(X,Y)
theta


# In[14]:


error_list


# In[15]:


plt.plot(error_list)
plt.show()


# In[21]:


y_hat= theta[0] + theta[1]*X
plt.plot(X,Y)
plt.plot(X,y_hat)


# In[ ]:




