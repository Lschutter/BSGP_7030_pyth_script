#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
get_ipython().system('pip install scikit-learn')


# In[2]:


from sklearn.linear_model import LinearRegression
data = pd.read_csv("regrex1.csv")
print(data)


# In[3]:


data_y = np.array(data.y)
data_x = np.array(data.x)
plt.scatter(data_x, data_y)
plt.show()


# In[4]:


x= np.array(data['x']).reshape((-1,1))
y= np.array(data['y'])
model = LinearRegression ()
model.fit (x, y)


# In[5]:


pred= model.predict(x)
plt.plot(data.x, pred, label = 'Linear Regression Model', color= "red")
plt.scatter(data_x, data_y, label='Scatter Plot')
plt.title("Linear Regression Model Python Assignment")
plt.legend()
plt.show()


# In[ ]:




