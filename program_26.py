#!/usr/bin/env python
# coding: utf-8

# In[25]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
t_explode = (0.0, 0.1, 0.0, 0.0, 0.0, 0.0)
daily_activity = ['Shower', 'Toilet', 'Leaks', 'other', 'Faucet', 'Clothes Washer']
usage_percent = [16.8, 26.7, 13.7, 5.3, 15.7, 21.7]
 
# Draw the pie chart
plt.pie(usage_percent,

        labels=daily_activity,

        autopct='%1.1f',explode = t_explode,

        startangle=90)
plt.show()

