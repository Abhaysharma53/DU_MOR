
import math
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))
series = 0
for i in range(1,n+1,4):
    series=series+(x**(i)/math.factorial(i))
for j in range(3,n+1,4):
    series=series-(x**(j)/math.factorial(j))
print("Value of Sinx using taylor's expansion is",series)
