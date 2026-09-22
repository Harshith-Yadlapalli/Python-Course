# FUNCTIONS

"""Function in Python
A function is a reusable block of code that performs a specific task. You write it once and can call it whenever you need it.
Small example :- """

def greet():
    print("Hello, Nayan!")
greet()

# ============================================================
# Function definition and function call
def addition(x, y):
    return x + y
print(addition(10, 20))
# Output:
# 30
# ============================================================
# WHY FUNCTIONS?
# ============================================================
# 1. Reusability
# 2. Complexity will be reduced
# 3. Maintaining modularity
# ============================================================
# TYPES OF FUNCTIONS
# ============================================================
# Built-in functions:
# len(), max(), min(), sum()

# User-defined functions:
# 1. With return & with parameters
# 2. With return & without parameters
# 3. Without return & with parameters
# 4. Without return & without parameters
# ============================================================
# 1. WITH RETURN & WITH PARAMETERS
# ============================================================
def addition(a, b):
    return a + b
print(addition(10, 20))
# Output:
# 30
# ============================================================
# 2. WITH RETURN & WITHOUT PARAMETERS
# ============================================================
def addition2():
    a = int(input())
    b = 10
    return a + b
print(addition2())
# Example input:
# 90
# Output:
# 100
# ============================================================
# 3. WITHOUT RETURN & WITH PARAMETERS
# ============================================================
def addition3(x, y):
    print(x + y)
a = addition3(9, 4)
print(a)
# Output:
# 13
# None
# ============================================================
# 4. WITHOUT RETURN & WITHOUT PARAMETERS
# ============================================================
def addition4():
    a = 4
    b = 5
    print(a + b)
a = addition4()
print(a)
# Output:
# 9
# None
# ============================================================
# POSITIONAL ARGUMENT
# ============================================================
def student(name, age):
    print(name)
    print(age)
student("Nayan", 20)
# Output:
# Nayan
# 20
# ============================================================
# KEYWORD ARGUMENT
# ============================================================
def student(name, age):
    print(name)
    print(age)
student(name="Nayan", age=20)
# Output:
# Nayan
# 20
# ============================================================
# DEFAULT ARGUMENT
# ============================================================
def addition(a, b, c=0, d=0):
    return a + b + c + d
print(addition(10, 20))
print(addition(10, 20, 30))
print(addition(10, 20, 30, 40))
# Output:
# 30
# 60
# 100
# ============================================================
# VARIABLE LENGTH ARGUMENT
# ============================================================
def addition(*var):
    print(type(var))
    total = 0
    for num in var:
        total += num
    return total
print(addition(10, 20, 30, 40))
# Output:
# <class 'tuple'>
# 100
# ============================================================
# VARIABLE LENGTH KEYWORD ARGUMENT
# ============================================================
def addition(**var):
    print(type(var))
    total = 0
    for num in var.values():
        total += num
    return total
print(addition(a=1, b=2, c=3))
# Output:
# <class 'dict'>
# 6