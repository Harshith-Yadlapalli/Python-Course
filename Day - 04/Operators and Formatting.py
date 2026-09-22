""" 7 types of operators in python
1. Arithmetic Operators ( +, -, *, /, %, **, // )
2. Comparison Operators (==, !=, >, <, >=, <=)
3. Logical Operators (and, or, not)
4. Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=, &=, |=, >>=, <<=)
5. Identity Operators (is, is not)
6. Membership Operators (in, not in)
7. Bitwise Operators (&, |, ^, ~, <<, >>)"""

#1. Arthematic Operators - 
#add - 
a=10 
b=20
c=a+b
print(c)  #output:- 30
#subtract -
d=a-b
print(d)  #output:- 10
#divide -
e=b/a
print(e)  #output:- 2.0
#multiply -
f=a*b
g=a//b
h=a/b
print(f)  #output:- 200
print(g)  #output:- 0
print(h)  #output:- 0.5

#2. Comparision operators - 
m= 90
n=100
print(m>n) 
print(m<n)
print(m==n)
print(m!=n)
print(m>=n)
print(m<=n)
print(m<=90)

#Logical operators - (and,or,not)

#1. and operators - 
#both conditions need to be true

age = 20
has_id = True
print(age >= 18 and has_id)

#2. or operator -
# any condition needs to be true
day = "Sunday"

print(day == "Saturday" or day == "Sunday")

#3. not operator - 
# not simply reverses the result
is_raining = True

print(not is_raining)

# Assignment operator - 
a =100 
a=a+2
a-=50
print(a)

# Identity operator - 
l1 = [10,20]
l2 = [10,20]
print(l1 is l2)   # different memory location
l3 = l1
print(l3 is l1)

#membership operator -
l = [10,20,30,40]
target = 30,50
print(target in l )
print(target not in l)

str_1 ="python"
print( "p" not in str_1)
d = {"a": 1,"b": 2,"c":3 }
print(a in d)
print(1 in d)

#bitwise oeprator - 
#  &operator - here both bits must be 1 
a = 5
b = 3
print(a & b)    #output - 1
# 5 = 101
# 3 = 011
#     ---
# &   001

""" |operator - here if atleast 1 bit is 1, then the result 1"""
a = 5
b = 3
print(a | b)
# 5 = 101
# 3 = 011
#     ---
# |   111

#xor bitwise
#xor gives 1 when the bits are different
a = 5
b = 3
print(a ^ b)
# 5 = 101
# 3 = 011
#     ---
# ^   110

#bitwise not(~)
a = 5
print(~a)
# ~n = -(n + 1)

#left shift <<
a = 5
print(a << 1)
#working - 
# 5 = 101
# 101 << 1
# = 1010

#right shift >>
m = 10
print(m >> 1)
#working - 
# 10 = 1010
# 1010 >> 1
# = 0101
# z9 = 90
# print(z9)