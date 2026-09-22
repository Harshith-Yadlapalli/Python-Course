"""What is List Comprehension? 

List comprehension is a short and simple way to create a new list from an existing list (or sequence).
Instead of writing a for loop with append(), you can do it in one line."""
#example :-
#normal way to write the code,
numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    result.append(i * 2)
print(result)
#list comprehension way to wirte the code in short :-
numbers = [1, 2, 3, 4, 5]
result = [i * 2 for i in numbers]
print(result)

#syntax :- 
# [Expression for x in iterable if condition]
#[x for x in l if x%2==0]

l=[1,2,3,4,5]
r=[]
for i in(l):
    r.append(i*2)
print(r)

#now, lets do it in list comprehension - 
l1 = [1, 2, 3, 4, 5]
r1 = [i * 2 for i in l1]
print(r1)

#list comprehension with if else -
l2=[1,2,3,4,5,6]
r2=["even" if x%2==0 else "odd"for x in l2]
print(r2)

#examples :- 
m = [[1,2,3],[4,5,6],[7,8,9]]
r =[(row,column)for row in range(len(m)) for column in range(len(m[row]))]
print(r)        # gives index as output

m1 = [[1,2,3],[4,5,6],[7,8,9]]
r1 =[m1[row][column]for row in range(len(m)) for column in range(len(m[row]))]
print(r1)        # gives list as an output


""" Generator :- It is a special type of Iterator to generate values lazily one by one"""
#What is a Generator?
#A generator is something that produces values one at a time, 
#instead of creating and storing all the values in memory at once.

def generator(n):
    yield 1             #yield is used in generator. it is similar to return,
    yield 2             #but yield gives one value at a time and pauses the function.
    yield 3
    yield 4
r5=generator(5)
print(next(r5))
print(next(r5))
print(next(r5))
print(next(r5))
# print(next(r5))       -> Stop Iteration 

list1 = [1,2,3,4]
result1 = tuple(x for x in list1)
print(type(result1))
print(result1)

list2=[1,2,34]
res2= (x for x in list2)
print(type(res2))
print(next(res2))
for i in res2:
    print(i, end = "$")

#example :- 
def generator(x):
    x=x+1
    yield x
    x+=10
    yield x 
    x+=20
    yield x
r5=generator(10)
for i in r5:
    print(i)