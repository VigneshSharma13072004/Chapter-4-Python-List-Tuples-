#  Write a program to add elements of List and get inputs from user 

numbers = []

for i in range(10):
 input_num = int(input(f"Enter the {i+1} elements of tuples : "))
 numbers.append(input_num)
print("List elements : ",numbers)
print("Sum of List elements : ",sum(numbers))
