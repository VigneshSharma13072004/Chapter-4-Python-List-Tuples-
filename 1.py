# Write a program to store 7 fruits in the list enter by user 
input_str = input("\nEnter the seven fruits name : ")
my_list = input_str.split()
my_list = [str(fruit) for fruit in my_list]
print("Fruits : ",my_list)

