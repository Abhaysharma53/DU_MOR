import cmath

def Quadroot(a,b,c):
    r=cmath.sqrt((b*b)-(4*a*c)) 
    root1=(r-b)/(2*a)
    root2=-(r+b)/(2*a)
    return root1,root2

print('The general form of quadratic equation is ax^2 + bx + c')
a=input("Enter value of a : ")
b=input("Enter value of b : ")
c=input("Enter value of c : ")
root_value=Quadroot(float(a),float(b),float(c)) 
print("So the values of square roots of the given equation is {}".format(root_value))