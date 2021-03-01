#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
#implementing the basic EOQ formula
c = float(input("enter the unit cost of the item  : "))
d = float(input("enter the annual Demand  : "))
a = float(input("Enter the annual Ordering Cost  : "))
i = float(input("enter the annual interest rate in percentage  : "))
H = (i*c)/100
quan = (2*a*d)/H
Q = math.sqrt(quan)
print("so the annual order quantity is {}".format(Q))

