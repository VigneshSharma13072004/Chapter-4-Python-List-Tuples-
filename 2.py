# Write a program to store 6 students marks and disply in a sorted methods

# Making a empty list
Marks = []

# Taking loop anf range upto 6 cause we want 6 inputs from user
for i in range(6):
 Student_marks = int(input(f"Enter the mark of {i+1} student :  "))
 Marks.append(Student_marks)
 Marks.sort()
print(Marks)