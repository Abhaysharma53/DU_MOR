#program to check the armstrong number
num = int(input('enter the number to find its armstrong number  : '))
num_copy = num
l = list()

while num_copy > 0:
    rem = num_copy%10
    l.append(rem)
    num_copy = int(num_copy/10)
#print(l)
digits = len(l)
arm_l = [i**digits for i in l]   #list comprehension alternatively we can make function for the same
#arm_l = lst_arm(l) # function call
arm_num = sum(arm_l)
if(arm_num == num):
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))



# the function which will be used to find power value of each element of list can be define as:
#lst1 = list()
#def lst_arm(lst):
#   for i in lst:
#        lst1.append(i**len(lst))
#    return lst1
