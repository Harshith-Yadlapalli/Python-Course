"""Recursion :- 1. base condition
                2. function call

Types of recursion:- 1. Direct recursion
                     2. Indirect recursion """

#sum of natural numbers 
def sum_of_natural_number(n):
    if n==1:
        return 1
    return n+sum_of_natural_number(n-1)
print(sum_of_natural_number(5))

#printing even numbers
def sum_of_even(n):
    if n%2==0:
        if n==2:
            return 2
        return n+sum_of_even(n-2)
    else:
        return sum_of_even(n+1)
print(sum_of_even(9))

#prime number checking
# num= int(input())
# def prime_number(n):
#     count= 0 
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#             return True
#     else:
#             return False
# print(prime_number(num))

#prime number from 2 to 100
l=[]
def prime_numbers(n):
    count = 0 
    for i in range(1, n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
for i in range(2,101):
    if prime_numbers(i):
        l.append(i)
print(l)


""" Lambda Function
 Anonymous function :- """ 
 # a function tht doesnt have a name 
def square (n):
    return n*n
square(10) 

#syntax :-          lambda argument : expression
#                          |
#                        keyword
square = lambda x:x*x
print(square(5))


"""Higher Order Function"""
# examples of higher order fucntions :-
#  filter(), map(), reduce()

# filter() - select items
# map() - change items
# reduce() - combines items

#filter example - 
numbers=[10,20,30,40,6,7,8,9,11]
r=filter(lambda x:x%2==0,numbers)
print(list(r))

numbers1 = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers1)
print(list(result))

#map example - 
a=[13,27,8,12,21,29]
q=map(lambda x:x+x,a)
print(list(q))

numbers2= [1, 2, 3, 4, 5]
result3 = map(lambda x: x ** 2, numbers2)
print(list(result3))

#reduce example -
from functools import reduce
y=[1,2,3,4,5]
p=reduce(lambda a,b :a+b,y)
print(y)

from functools import reduce
numbers5 = [1, 2, 3, 4, 5]
result5 = reduce(lambda x, y: x + y, numbers5)
print(result5)