# Write a program to store seven cigratte name and make a list
# ONE WAY
'''Cigratte = []
L1 = input("Enter the Cigratte you want : ")
Cigratte.append(L1)
L2 = input("Enter the Cigratte you want : ")
Cigratte.append(L2)
L3 = input("Enter the Cigratte you want : ")
Cigratte.append(L3)
L4 = input("Enter the Cigratte you want : ")
Cigratte.append(L4)
L5 = input("Enter the Cigratte you want : ")
Cigratte.append(L5)
L6 = input("Enter the Cigratte you want : ")
Cigratte.append(L6)
L7 = input("Enter the Cigratte you want : ")
Cigratte.append(L7)
print(Cigratte)'''

# Second Way

Cigratte = []  # Taking a empty List
for i in range(7): # Cause we want to take input 7 times
    L = input(f"Enter the Cigratte name :  ")
    Cigratte.append(L)
print("List of & Cigrattes : ",Cigratte)
