#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python


# In[16]:


#coding: utf-8


# In[3]:


#python linear model script assignment


# In[4]:


from matplotlib import pyplot as plt


# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[7]:


import sklearn


# In[8]:


from sklearn.linear_model import LinearRegression


# In[9]:


import sys


# In[10]:


import csv


# In[11]:


if len (sys.argv) < 2:
    sys.exit(1)


# In[12]:


argument = sys.argv[1]
t=[]
x1=[]
y1=[]


# In[13]:


with open (argument ,'r', newline='') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        x1.append(row[1])
        y1.append(row[0])


# In[14]:


x2 = np.array(x1, dtype= float)
y2 = np.array(y1, dtype= float)


# In[15]:


plt.scatter(x2, y2)
plt.show()
plt.savefig('py_orig.png')


# In[17]:


plt.scatter(x2, y2)


# In[18]:


plt.show()


# In[19]:


plt.savefig('py_orig.png')


# In[20]:


x= np.array(x2).reshape((-1))


# In[21]:


y= np.array(y2)


# In[22]:


model = LinearRegression ()


# In[24]:


model.fit (x, y)


# In[25]:


pred= model.predict(x)


# In[26]:


plt.plot(x2, pred, label = 'Linear Regression Model', color = "red")


# In[27]:


plt.scatter(x2, y2, label = 'Scatter Plot' = "blue")


# In[28]:


plt.title("Linear Regression Model Assignment - Pyth")


# In[29]:


plt.xlabel ("x Data")


# In[30]:


plt.ylabel("Y Data")


# In[31]:


plt.legent()


# In[32]:


plt.show()


# In[33]:


plt.savefig('py_lm.png


# In[ ]:




