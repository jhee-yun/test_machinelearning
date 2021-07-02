#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[3]:


pickle.load(open('./saves/favorite_save.pkl','rb'))


# In[5]:


favorite_load = pickle.load(open('./saves/favorite_save.pkl','rb'))
print(favorite_load)


# In[6]:


type(favorite_load)


# In[7]:


print(favorite_load['tiger'])


# In[9]:


autompg_lr = pickle.load(open('./saves/autompg_lr.pkl','rb'))
print(autompg_lr)


# In[10]:


type(autompg_lr)


# In[11]:

# input from outside
a = 3504.0
b = 8
import numpy as np
pre = np.array([[a,b]])
print(autompg_lr.predict(pre))

print(autompg_lr.predict([[3504.0,8]]))


# In[ ]:




