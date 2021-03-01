#!/usr/bin/env python
# coding: utf-8

# In[2]:


#program to enter the 5 subjects marks and then print grade
score = list()
for i in range(5):
    sub = int(input("enter the score : "))
    score.append(sub)
avg = sum(score)/5    
if (avg < 34):
    print("your rewarded grade is E")
elif (avg > 34 and avg < 50):
    print("your rewarded grade is D")
elif (avg > 50 and avg < 70):
    print("your rewarded grade is C")
elif (avg > 70 and avg < 90):
    print("your rerwarded grade is B")
else:
    print("your rewarded grade is A ")


    

