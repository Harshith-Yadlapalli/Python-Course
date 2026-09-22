#local scope
def f1():
    x = 10
    print(x)
f1()

#global scope

x=20
def f2():
    print(x)
f2()
print(x)

#enclosing scope
def f4():
    x=100
    def f5():
        y=200
        print(y)
    f5()
f4()

#built in scope 
def f6():
    a=[12,8,10,20]
    return sum(a)
print(f6())

#changing global value
x=20
def f2():
    global x
    x=x+20
    print(x)
f2()

#pass by object reference
def modify_number(x):
    x = x + 10
    print("Inside function:", x)
num = 5
modify_number(num)
print("Outside function:", num)

#example 2 pass by object reference
def md(x):
    x=20
    print(id(x))
    print(x)
a=10
print(id(a))
md(a)

#example 3 pass by object reference
def f(x):
    x= [10,20,30]
    print(id(x))
    print(x)
a= [1,2,3]
print(id(a))
f(a)

#exxample -
def f(a):
    a.append(5)
    print(id(a))
    print(a)
b=[1,2,3,4]
print(id(b))
f(b)


#example:- 
def f(l):
    l.append(10)
    l=[1,2,3,4]
    print(id(l))
    print(l)
k= [1,2,3,4]
print(id(k))
f(k)                    #output:- [1,2,3,4]


#recursion function
#a function which calls itself is called recursion function

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)       #here in this line we are calling the same fucntion(factorial) again 
print(factorial(5))