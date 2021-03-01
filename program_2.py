num1 = int(input('enter the first number : '))
num2 = int(input('enter the second number : '))
while True:
    print('a : for additon(+)')
    print('b : for substraction(-)')
    print('c : for multiplication(*)')
    print('d : for division(/)')
    print('e : for integer division(//)')
    print('f : for modulo(%)')
    print('enter any other Alphabet to Exit')
    choice = input('enter your choice : ')
    if choice == 'a':
        print(num1 + num2)
    
    elif choice == 'b':
        print(num1 - num2)
    
    elif choice == 'c':
        print(num1 - num2)
    
    elif choice == 'd':
        print(num1 / num2)
    
    elif choice == 'e':
        print(num1 // num2)

    
    elif choice == 'f':
        print(num1 % num2)
    
    else:
        break
print('you have successfully exited from the program')
        
    
    