#fibonacci using recursion
def fib(term):
    if (term == 0 or term == 1):
        return term
    else:
        return (fib(term - 1) + fib(term - 2))

#take input from the user
m = 0
nterms = int(input("enter the no. of terms to print the fibonacci till that number  : "))
if(nterms <= 0):
    print("invalid choice!!! please try again")
else:
    for i in range(nterms):
        print(fib(m))
        m = m+1


#fibonacci using loop
#num1 =0
#num2 = 1
#nterms = int(input("enter the no of terms to print the fibonacci series  : "))
#if(nterms <= 0):
#    print("Invalid choice!!! please try again")
#else:
#    for i in range(nterms):
#        if(i <= 1):
#            total = i 
#        else:
#            total = num1+num2
#            num1 = num2
#            num2 = total
#        print(total)