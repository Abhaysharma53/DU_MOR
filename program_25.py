#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
x_coordinate = range(-50, 51)
y_coordinate = [x*x for x in x_coordinate]
plt.plot(x_coordinate, y_coordinate)
plt.show()

