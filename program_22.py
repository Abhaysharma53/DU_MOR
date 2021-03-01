#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creating dataframe of student info. taking value from user
import pandas as pd
roll_no = list()
name = list()
maths = list()
n = int(input("enter the no of students to store the information"))
for i in range(n):
    roll = input("enter the roll no of the {} student : ".format(i+1))
    roll_no.append(roll)
    nm = input("enter the student's name: ")
    name.append(nm)
    mat = int(input("enter their maths marks : "))
    maths.append(mat)
    print()

b = {'roll_no' : roll_no, 'Name' : name, 'Score' : maths}
c = pd.DataFrame(b)
print(c)
print(type(c))


# In[ ]:




