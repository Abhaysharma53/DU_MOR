#!/usr/bin/env python
# coding: utf-8

# In[14]:


i = 1
while i <= 5:
    j=1
    while j <= 5-i:
        print(" ", end=" ")
        j = j+1
    k=1
    while k <= i:
        print(j, end=" ")
        k = k+1
        j = j+1
    print()
    i=i+1
    




