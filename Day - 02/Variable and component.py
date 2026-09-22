# python installation ---> python org ---> (64-bit) python path
#cmd (IDLE python 64bit)

# ---> jupyter(python -n notepad)
#   3.14.7 version 

#Variable:-

x= 10
print(x)

# #rules 
# alphablets (small, capital)
# include numbers 
# can use underscores 
# number cant be used at the start of the variable name
# can use underscore anywhere

#single line comment :- 
# is used to comment out a single line of code

#Tokens:-  
num  =   10
# everything is seperated token each and every part (num,=,10)

#Identifiers :- 
#functions -> def f_name():
#Keywords -> if,else,elif,for,while,break,continue,return
#variables -> we give it 
#classes -> class class_name:
#objects -> object_name = class_name()

#assigning :-
x=2
#now python takes the x value as 2, becuase the value is assigned using the = symbol

#swapping :- 
x=10
y=20
temp = x
x=y 
y=temp
print(x,y)

#swapping but without using temp variable
x,y = 30,40
print(x,y)
x,y = y,x
print(x,y)
#python is dynamically typed language, so we can change the value of the variable at any time

#by using del we can delete the variable from the memory
z=100
print(z)