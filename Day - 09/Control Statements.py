# ============================================================
# CONTROL STATEMENTS IN PYTHON
# ============================================================
# Control statements control the flow of execution of a program.
# There are mainly 3 types of control statements:
# 1. Conditional statements
#       -> if
#       -> if-else
#       -> if-elif-else
#       -> nested if
# 2. Looping statements
#       -> for loop
#       -> while loop
# 3. Jump statements
#       -> break
#       -> continue
#       -> pass
# ============================================================
# 1. CONDITIONAL STATEMENTS
# ============================================================
# Conditional statements are used to make decisions.
# if
# if-else
# if-elif-else
# nested if

# Example:
age = 20
if age >= 18:
    print("You are an adult")
# ============================================================
# 2. LOOPING STATEMENTS
# ============================================================
# Loops are used to execute a block of code repeatedly.
# Two main types:

# 1. for loop
# 2. while loop
# ============================================================
# FOR LOOP
# ============================================================
# A for loop is used to iterate over an iterable.
#
# Syntax:

# for variable in iterable:
#     statement
# Iterables can include:
# list
# tuple
# string
# range
# dictionary
# set
# ------------------------------------------------------------
# Example 1: Loop through a list
# ------------------------------------------------------------
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)
# ------------------------------------------------------------
# Example 2: Loop through a tuple
# ------------------------------------------------------------
numbers = (10, 20, 30, 40)
for number in numbers:
    print(number)
# ------------------------------------------------------------
# Example 3: Loop through a string
# ------------------------------------------------------------
name = "Python"
for character in name:
    print(character)
# ------------------------------------------------------------
# Example 4: Loop through a range
# ------------------------------------------------------------
for number in range(5):
    print(number)
# Output:
# 0
# 1
# 2
# 3
# 4
# ============================================================
# RANGE FUNCTION
# ============================================================
# range(start, stop, step)

# start -> starting value (included)
# stop  -> ending value (excluded)
# step  -> amount to increase/decrease

# Example:
for number in range(1, 11):
    print(number)
# Prints numbers from 1 to 10.
# Example: print numbers from 1 to 20
for number in range(1, 21):
    print(number)
# Example: print even numbers
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
# Example: print numbers with a step of 2
for number in range(1, 11, 2):
    print(number)
# Output:
# 1
# 3
# 5
# 7
# 9
# ============================================================
# NATURAL NUMBERS
# ============================================================
# Natural numbers generally start from 1.
# Example:
# 1, 2, 3, 4, 5, ...
# Example: print first 20 natural numbers
n = 20
for number in range(1, n + 1):
    print(number)
# ------------------------------------------------------------
# Print even natural numbers from 1 to n
# ------------------------------------------------------------
n = 20
for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)
# ------------------------------------------------------------
# Print even numbers from 0 to 99
# ------------------------------------------------------------
for number in range(100):
    if number % 2 == 0:
        print(number)
# Another cleaner way:
for number in range(0, 100, 2):
    print(number)
# ============================================================
# LOOPING THROUGH A LIST USING INDEX
# ============================================================
# We can use range() and len() to access list elements
# using their indexes.
numbers = [26, 12, 7, 17, 27, 15, 16, 22]
for index in range(len(numbers)):
    print(numbers[index])
# Example:
# index 0 -> numbers[0]
# index 1 -> numbers[1]
# index 2 -> numbers[2]
# ============================================================
# SEARCHING FOR A VALUE IN A LIST
# ============================================================
# Example from the notebook:
# Find a target value in a list.
data = [26, 12, 7, 17, 27, 15, 16, 22]
target = 17
for index in range(len(data)):
    if data[index] == target:
        print("Target found at index:", index)
# A simpler way:
if target in data:
    print("Target found")
# ============================================================
# FOR LOOP WITH ELSE
# ============================================================
# Python allows an else block with a for loop.
# The else block executes when the loop finishes normally.

# If the loop is stopped using break,
# the else block does NOT execute.

# Example:
for number in range(5):
    print(number)
else:
    print("Loop completed")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed
# ============================================================
# WHILE LOOP
# ============================================================
# A while loop repeatedly executes code
# as long as the condition is True.

# Syntax:
# while condition:
#     statement
# Example:
number = 1
while number <= 5:
    print(number)
    number += 1
# Output:
# 1
# 2
# 3
# 4
# 5
# ------------------------------------------------------------
# Another while loop example
# ------------------------------------------------------------
count = 5
while count > 0:
    print(count)
    count -= 1
# ============================================================
# JUMP STATEMENTS
# ============================================================
# Jump statements change the normal flow of a loop.
# 1. break
# 2. continue
# 3. pass
# ============================================================
# 1. BREAK STATEMENT
# ============================================================
# break immediately terminates the loop.
# Example:
for number in range(10):
    if number == 5:
        break
    print(number)
# Output:
# 0
# 1
# 2
# 3
# 4
# The loop stops as soon as number becomes 5.
# ------------------------------------------------------------
# Break example from the notebook
# ------------------------------------------------------------
for number in range(10):
    if number == 5:
        break
    print(number)
# ============================================================
# BREAK WITH WHILE LOOP
# ============================================================
number = 1
while True:
    print(number)
    if number == 5:
        break
    number += 1
# ============================================================
# 2. CONTINUE STATEMENT
# ============================================================
# continue skips the current iteration
# and moves to the next iteration.

# Example:
for number in range(10):
    if number == 5:
        continue
    print(number)
# Output:
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 5 is skipped because continue was executed.
# ------------------------------------------------------------
# Continue example: print only odd numbers
# ------------------------------------------------------------
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
# Output:
# 1
# 3
# 5
# 7
# 9
# ============================================================
# 3. PASS STATEMENT
# ============================================================
# pass does nothing.
# It is used as a placeholder when we want to write
# a block of code later.

# Example:
for number in range(10):
    if number % 2 == 0:
        pass
    else:
        print(number)
# Here, pass simply does nothing when the number is even.

# Another example:
def future_function():
    pass
# We can add the actual code later.
# ============================================================
# FACTORS OF A NUMBER
# ============================================================
# A factor of a number is a number that divides it
# completely without leaving a remainder.

# Examples:
# Factors of 1:
# 1
# Factors of 2:
# 1, 2
# Factors of 3:
# 1, 3
# Factors of 4:
# 1, 2, 4
# Factors of 5:
# 1, 5
# Factors of 6:
# 1, 2, 3, 6
# Factors of 7:
# 1, 7
# Factors of 8:
# 1, 2, 4, 8
# Factors of 9:
# 1, 3, 9
# Factors of 10:
# 1, 2, 5, 10
# ------------------------------------------------------------
# Program to find factors of a number
# ------------------------------------------------------------
number = int(input("Enter a number: "))
for factor in range(1, number + 1):
    if number % factor == 0:
        print(factor)
# ============================================================
# PRIME NUMBER CHECK
# ============================================================
# A prime number has exactly two factors:
# 1 and itself.
# Examples:
# 2, 3, 5, 7, 11, 13...

# Program to check whether a number is prime.
number = int(input("Enter a number: "))
if number < 2:
    print("Not a prime number")
else:
    for factor in range(2, number):
        if number % factor == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
# ============================================================
# COUNT FACTORS OF A NUMBER
# ============================================================
number = int(input("Enter a number: "))
count = 0
for factor in range(1, number + 1):
    if number % factor == 0:
        count += 1
print("Number of factors:", count)
# ============================================================
# CHECK EVEN NUMBERS USING PASS
# ============================================================
for number in range(10):
    if number % 2 == 0:
        pass
    else:
        print(number)
# ============================================================
# FOR LOOP VS WHILE LOOP
# ============================================================
# FOR LOOP
# -> Used when we know what we want to iterate over.

# Example:
# for number in range(5):
#     print(number)
# WHILE LOOP
# -> Used when repetition depends on a condition.
# Example:
# number = 1
# while number <= 5:
#     print(number)
#     number += 1
# ============================================================
# BREAK vs CONTINUE vs PASS
# ============================================================
# break
# -> Completely stops the loop.
# continue
# -> Skips the current iteration.
# pass
# -> Does nothing; acts as a placeholder.
# ============================================================
# QUICK REVISION
# ============================================================
# CONTROL STATEMENTS
# 1. Conditional statements
#    -> if
#    -> if-else
#    -> if-elif-else
#    -> nested if
# 2. Looping statements
#    -> for
#    -> while
# 3. Jump statements
#    -> break
#    -> continue
#    -> pass
# ============================================================
# IMPORTANT:
# ============================================================
# range(10)
# -> 0 to 9
# range(1, 10)
# -> 1 to 9
# range(1, 11)
# -> 1 to 10
# range(1, 11, 2)
# -> 1, 3, 5, 7, 9
# range(10, 0, -1)
# -> 10, 9, 8, ..., 1
#range(1,0,9)