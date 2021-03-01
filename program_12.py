a = input("enter the String which you want to check  : ")
l = list()
count = 0
for i in range(len(a)):
    l.append(a[i])
lcopy = l.copy()
l.reverse()
print(l)
print(lcopy)
#another for comparison
for i in range(len(l)):
    if(l[i] == lcopy[i]):
        count=count+1
if(count == len(l)):
    print("string is palindrome")
else:
    print("string is not a palindrome")