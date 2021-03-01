#!/usr/bin/env python
# coding: utf-8

# In[14]:


#line of the form y =mx+b
#implementing the formula for the least square
import numpy as np
import matplotlib.pyplot as plt

def draw_line(x,y,b,m):
    plt.scatter(x, y, color = "m", marker = "o")
    y_pred = b + m*x
    plt.plot(x,y_pred, color = 'g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
def predict(x):
    return (b + m*x)
x = np.array([65,66,67,67,68,69,70,72])
y = np.array([67,68,65,68,72,72,69,71])
plt.scatter(x,y)
plt.show()    
n = len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)
dev_xy = np.sum(y*x) - n*mean_x*mean_y
dev_xx = np.sum(x*x) - n*mean_x*mean_x
m = dev_xy/dev_xx
print("slope of the line is {}".format(m))
b = mean_y - m*mean_x
print("intercept of the line is {}".format(b))
draw_line(x,y,b,m)
score = predict(66)
print(score)

