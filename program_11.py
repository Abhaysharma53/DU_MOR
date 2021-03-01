l = list()
biggest = 0
size = int(input("enter the no of elements that you want to enter to start  : "))
for i in range(size):
    t = int(input("enter the {} element  : ".format(i+1)))
    l.append(t)
print(l)
#print(len(l))
for i in range(len(l)):
    if(l[i] > biggest):
        biggest = l[i]
    else:
        continue
print("so the greatest number is {}".format(biggest))