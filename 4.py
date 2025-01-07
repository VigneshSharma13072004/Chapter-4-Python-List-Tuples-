#  Write a program to count number of given elements in tuple 

Tuple_elements = input("Enter the elements of tuple using space  : ")
user_input = Tuple_elements.split()
print("Tuple elements : ",user_input)
X = input("Enter the element you want to search: ")
print(f" {X} is repeating {user_input.count(X)} times in tuple.")
