#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print(""" Notation for a M/M/C System
l = Arrival rate
mu = Service rate
c = Number of servers in the system
n = Number of customers in the system
Pn = Probability of n customers in the system
Lq = Expected number of customers in the queue
L = Expected number of customers in the system
Wq = Expected time spent in the queue
W = Expected time spent in the system
rho = Traffic intensity """)
l = float(input("Enter the arrival rate : "))
mu = float(input("Enter the service rate : "))
c = int(input("Enter the number of servers : "))
rho = l/(mu*c)
r = l/mu
print("Traffic intensity is", rho)
if(rho>=1):
    print("The system can never reach a steady state")
else:
    print("The system can reach a steady state with the following performance measures.")
print()
t = 0
print("Calculation of P0")
for i in range(0,c):
    t = t + ((r**i)/(math.factorial(i)))
print(t)
s = ((r**c)/((math.factorial(c))*(1-rho)))
print(s)
P0 = (s+t)**(-1)
print( "Value of P0 is", P0)
print()
print("Calculation of Pn")
n=int(input("Enter the value of n : "))
if(n>=0 and n<c):
    Pn = ((l**n)/((math.factorial(n))*(mu**n)))*P0
elif(n>=c):
    Pn = ((l**n)/((math.factorial(c))*(mu**n)*(c**(n-c))))*P0
else:
    print("Invalid")
print("Probability of",n,"customers in the system is", Pn)
print()
print("So the Measure of Performace are")
print()
Lq = (((r**c)*rho)/((math.factorial(c))*((1-rho)**2)))*P0
print("Expected number of customers in the queue are", Lq)
print()
L = r + Lq
print("Expected number of customers in the system are", L)
print()
Wq = Lq/l
print("Expected time spent in the queue is", Wq)
print()
W = Wq + ((1/mu))
print("Expected time spent in the system is",W)

