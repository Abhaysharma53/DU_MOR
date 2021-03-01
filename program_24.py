#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt

year = [2016, 2017, 2018, 2019, 2020]
percent_result = [74.87, 85.97, 81.03,  85.82, 98.97]
plt.bar(year, percent_result)
plt.title("Performace of students in five consecutive years")
plt.xlabel("Year")
plt.ylabel("Percentage Marks")
plt.show()

