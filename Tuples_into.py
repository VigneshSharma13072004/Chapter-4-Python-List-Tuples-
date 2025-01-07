# here the tuple is written in ( ) brackets and it is immutable 
a = (1,2,3,4,"shivam",3.2)
#  printing a will give you tuple elements
print(a)

#  SOME MORE METHODS OF TUPLE
# Count method will return the number of time element is repeating 
x = (1,1,2,3,4,1,56,78754,"hey","hllo")
countnum = x.count(1)
print(countnum)

# index method will return the index value of given number
y = (1,0,2,3)
index_value = y.index(0)
print(index_value)

# Concatenation is use to add two tuples
T1 = (1,2,3,4,5)
T2 = (6,7,8,9,10)
ADD_T1_T2 = T1 + T2
print(ADD_T1_T2)

