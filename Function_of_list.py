# SORT funtion is use to sort the list in asceneding order

L1 = [2,3,8,12,34,9,15]
L1.sort()
print(L1)

# reverseing the string
L2 = [1,2,3,4,5,6,7]
L2.reverse()
print(L2)
# append is use to add any elements at last
L3 = [1,2,3]
L3.append(111)
print(L3)
# insert is use to add a element at specific index
L4 = [5,6,7,9]
L4.insert(3,8)
print(L4) 
#  index function return the index value of given string

input_str = input('Enter the list elemenets : ')
my_list = input_str.split()
my_list = [int(num)  for num in my_list]
print("\nList : ",my_list)
print(my_list.index(2))
