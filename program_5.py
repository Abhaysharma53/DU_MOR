import math
num = int(input("enter the number to proceed further : "))
count = 0
while True:
    print('a: to check whether the number is odd or even')
    print('b: to check whether the number is prime or not')
    print('enter any other alphabet to exit from the program')
    choice = input('enter your choice   ')
    
    if choice == 'a':
        if (num%2 == 0):
            print('{} is even'.format(num))
        else:
            print('{}  is odd'.format(num))
    
    elif choice =='b':
        if (num > 1):
            if(num == 2):
                print('{} is a prime number'.format(num))
            elif (num > 2):
                for i in range(2, math.ceil((num+1)/2)):
                    if ((num%i) == 0):
                        count = count+1
                if (count == 0):
                    print("{} is prime".format(num))
                else:
                    print(" {} is not prime".format(num))
                                                         
                    
        else:
            print('invalid choice .. please try again')
    else:
        break
print('you have successfully exited from the program')
    