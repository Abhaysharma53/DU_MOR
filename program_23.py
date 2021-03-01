#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print(df.mean())
print(df.describe(include = 'all'))
print()
print("skewness of the data is")
skew_value = df.skew(axis =0)
print(skew_value)
print()
print("kurtosis of the data is")
kurt_value = df.kurt(axis =0)
print(kurt_value)

