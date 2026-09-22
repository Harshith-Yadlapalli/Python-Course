# Data types
# 1. Numeric data types - integers, floats, complex numbers(4i+j)
# 2. Sequence data types - strings, lists, tuples
# 3. Mapping data types - dictionaries
# 4.Boolean data types - True or False
# 5. None data type - None

#sequence data types
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
string1 = "Hello, World!"
print(list1)
print(tuple1)
print(string1)

#mapping data types
dict1 = {"a": 1, "b": 2, "c": 3}
details = {"name": "John", "age": 30, "city": "New York"}
print(details["city"])

#set data types
set1 = {1, 2, 3, 4, 5}
#set only takes unique values, so if we add duplicate values, it will only keep one instance of that value
set2 = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print(set2)
s = {10,1,2,10,5}
print(s)

#Boolean data types
a = True
print(a)
#true/false values can be used in conditional statements
#None type - none
#       {} ---> none
#       () ---> none
#          empty

list=["abc", 34, True, 40, "male"]
array = [1, 2, 3, 4, 5]

#length 
print(len(list))

#list is mutable data type
#it can store diff. type of data types or same data types
#memory is allocated dynamically for list, so we can add or remove elements from the list
#we can use indexing to access elements of the list
#we use index to change the value of an element in the list
ll= [1, 2, 3, 4, 5]
ll[3] = 5
print(ll)
#list can contain duplicate values
#we can add and del elements from the list

#tuple :- 

t = (1, 2, 3, 4, 5)
#tuple is immutable data type
#we cant change the value of an element in the tuple
#we cant add or modify elements in the tuple
#we can take duplicate values in the tuple

#strings :-
s = "1 2 3 4 5 "
#string is immutable data type
#we cant change the value of an element in the string

#common in all list,tuple,string we use square brackets to access the elements of the list,tuple,string
# print(L[0]) #accessing the first element of the list

#in sets:- 
# 1.it has unique values
# 2.it is unordered data type
#3. it is mutable data type

s={1,2,3,3,4,3,4,1}
print(s)

#dictionary :- 
# 1. it is mutable data type
# 2. it is unordered data type
#3. it has key-value pairs
d = {"a": 1, "b": 2, "c": 3}
print(d["c"])

#type conversion 

#changing data types from one to another is called type conversion
#they are two types of type conversion :- 
#1. implicit type conversion - done by python automatically
#2. explicit type conversion - done by the programmer

#Implicit type conversion - 
x= 10
y=9.5
print(x+y)

#explicit type conversion -
s1= "123"
x=int(s1)
print(type(x))

#explicit is done by us (user)
#we define the data type we want to convert to.

s0="123"
print(s0)