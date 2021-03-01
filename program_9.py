def fact(num):
    if (num == 1):
        return num
    else:
        return (num * fact(num -1))

#starting with the user input
number = int(input("enter the number to find its factorial  : "))
if(number == 0):
    print("the factorial of {} is 1".format(number))
elif(number < 0):
    print("the factorial of the negative numbers can not be computed")
else:
    print("the factorial of {} is {}".format(number, fact(number)))
    