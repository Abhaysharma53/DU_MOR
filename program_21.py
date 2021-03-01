#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
fields = ['Name', 'attendance%', 'CGPA']

data = [['Abhay', 87.2, 8.9 ],
       ['Anas', 83, 7.7],
       ['Himangi', 98, 9.3],
       ['Ajay', 81, 8.4],
       ['Aman', 79, 8.2]]
file_name = 'Student_records.csv'

with open(file_name, 'w')as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
    
#iterating over the same file in reading mode
with open(file_name, 'r')as file:
    csvreader = csv.reader(file)
    for line in csvreader:
        print(line)
        


# In[ ]:




