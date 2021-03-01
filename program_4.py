num = int(input("enter the number to proceed further :  "))
l = list()
while num > 0:
    rem = num%10
    l.append(rem)
    num = int(num/10)
#print(l)
while True:
    print('a : to reverse the number entered ')
    print('b : to print the sum of the digit ')
    print('enter any other alphabet to exit')
    choice = input('enter your choice :  ')
    
    if choice == 'a':
        print('the reverse of the number is ')
        print(*l, sep = '')
    elif choice == 'b':
        print('the sum of the digit of the number is : {}'.format(sum(l)))
    else:
        break

print("you have successfully exited from the program")