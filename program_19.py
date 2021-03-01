#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import math
a = np.array([0,1,2,3,4,5])
b = np.array([42, 33, 14, 6, 4, 1])
fx = a*b
f = np.sum(b)
m = np.sum(fx)/f
print("so the mean of the data is {}".format(m))   #mean of the data
N = list()
prob = list()
for i in a:
    px = (((math.exp(-m))*(m**i))/(math.factorial(i)))
    prob.append(round(px,4))
    exp_f = round(px*f)
    N.append(exp_f) 
print("******so the expected frequency and the associated probability according to the poisson distribution is *****")
print(a)
print(N)
print(prob)

