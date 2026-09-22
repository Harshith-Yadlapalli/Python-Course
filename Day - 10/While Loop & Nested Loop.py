# ============================================================
# CONTROL STATEMENTS - LOOPS
# ============================================================
# Control statements control the flow of execution of a program.
# Main types:
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
# WHILE LOOP
# ============================================================
# A while loop repeatedly executes a block of code
# as long as the condition is True.

# Syntax:
# while condition:
#     statement
# ------------------------------------------------------------
# Example 1: Print numbers from 1 to 10
# ------------------------------------------------------------
i = 1
while i <= 10:
    print(i)
    i += 1  # Increase i by 1 after every iteration
# Output:
# 1
# 2
# 3
# ...
# 10
# IMPORTANT:
# If we forget to update i, the loop may become infinite.

# Example:
# i = 1
# while i <= 10:
#     print(i)

# i never changes, so the condition always remains True.
# ============================================================
# WHY DO WE USE A WHILE LOOP?
# ============================================================
# A while loop is useful when the number of repetitions
# is controlled by a condition.
# We often use it when we don't know beforehand
# exactly how many times the loop needs to run.
# ------------------------------------------------------------
# Example 2: Countdown
# ------------------------------------------------------------
count = 5
while count >= 1:
    print(count)
    count -= 1  # Decrease count by 1
# Output:
# 5
# 4
# 3
# 2
# 1
# ------------------------------------------------------------
# Example 3: User-controlled loop
# ------------------------------------------------------------
number = int(input("Enter a positive number: "))
while number > 0:
    print("You entered:", number)
    number = int(input("Enter another positive number: "))
print("Loop ended")
# The loop continues until the user enters 0 or a negative number.
# ============================================================
# COUNT THE NUMBER OF DIGITS
# ============================================================
# Example from the notebook:
# n = 2026
# We repeatedly divide the number by 10.
# Every division removes one digit.
# 2026 -> 202 -> 20 -> 2 -> 0
# Therefore, there are 4 digits.
n = 2026
count = 0
while n > 0:
    count += 1
    n = n // 10  # // gives the integer quotient
print("Number of digits:", count)
# ------------------------------------------------------------
# User input version
# ------------------------------------------------------------
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("Number of digits:", count)
# ============================================================
# SUM OF DIGITS
# ============================================================
# Example:
# Number = 234
# 2 + 3 + 4 = 9
# We can extract the last digit using % 10.
# Then remove the last digit using // 10.
n = int(input("Enter a number: "))
total = 0
while n > 0:
    digit = n % 10       # Gets the last digit
    total = total + digit
    n = n // 10          # Removes the last digit
print("Sum of digits:", total)
# Example:
# n = 234
# digit = 4 -> total = 4
# digit = 3 -> total = 7
# digit = 2 -> total = 9
# ============================================================
# SUM OF DIGITS USING STRING
# ============================================================
# Another way to calculate the sum of digits
# is to convert the number into a string.
n = 234
string = str(n)
total = 0
for ch in string:
    total = total + int(ch)  # Convert each character to integer
print("Sum of digits:", total)
# Output:
# 9
# ============================================================
# STRING CONCATENATION
# ============================================================
# String concatenation means joining two or more strings
# together using the + operator.
s1 = "yadavg"
s2 = "nayan"
s3 = s1 + s2

print(s3)
# Example:
# "Hello" + "World"
# -> "HelloWorld"
# ------------------------------------------------------------
# Concatenating with a space
# ------------------------------------------------------------
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)
# Output:
# Hello World
# ============================================================
# CONVERT STRING TO UPPERCASE
# ============================================================
# The .upper() method converts a string to uppercase.
string = "nayan"
result = ""
for ch in string:
    result = result + ch.upper()
print(result)
# Output:
# NAYAN
# ------------------------------------------------------------
# Easier way using .upper()
# ------------------------------------------------------------
string = "nayan"
print(string.upper())
# Output:
# NAYAN
# ============================================================
# FOR LOOP VS WHILE LOOP
# ============================================================
# FOR LOOP
# -> Generally used when iterating over a sequence/range.
# Example:

# for i in range(5):
#     print(i)
# WHILE LOOP
# -> Runs while a condition remains True.
# Example:
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# ============================================================
# JUMP STATEMENTS
# ============================================================
# Jump statements change the normal flow of a loop.
# 1. break
# 2. continue
# 3. pass
# ============================================================
# BREAK
# ============================================================
# break immediately stops the loop.
for i in range(10):
    if i == 5:
        break  # Stop the loop when i becomes 5
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# ============================================================
# CONTINUE
# ============================================================
# continue skips the current iteration
# and moves to the next iteration.
for i in range(10):
    if i == 5:
        continue  # Skip 5
    print(i)
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
# ============================================================
# PASS
# ============================================================
# pass does nothing.
# It is mainly used as a placeholder.
for i in range(10):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
# ============================================================
# FACTORS OF A NUMBER
# ============================================================
# A factor is a number that divides another number
# completely without leaving a remainder.
# Examples:
# 1  -> 1
# 2  -> 1, 2
# 3  -> 1, 3
# 4  -> 1, 2, 4
# 5  -> 1, 5
# 6  -> 1, 2, 3, 6
# 7  -> 1, 7
# 8  -> 1, 2, 4, 8
# 9  -> 1, 3, 9
# 10 -> 1, 2, 5, 10
# ------------------------------------------------------------
# Find factors using a for loop
# ------------------------------------------------------------
number = int(input("Enter a number: "))
for factor in range(1, number + 1):
    if number % factor == 0:
        print(factor)
# ============================================================
# FIND MAXIMUM VALUE USING A LOOP
# ============================================================
# List from the notebook:
numbers = [10, 2, 45, 26]
# Steps:
# 1. Consider the first element as the maximum.
# 2. Check every other element.
# 3. Compare the current element with maximum.
# 4. If current element is greater, update maximum.
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print("Maximum:", maximum)
# Output:
# Maximum: 45
# ------------------------------------------------------------
# Python's built-in max() function
# ------------------------------------------------------------
numbers = [10, 2, 45, 26]
print(max(numbers))
# Output:
# 45
# ============================================================
# WHILE LOOP - FIND FACTORS
# ============================================================
# The same factor problem can also be solved using
# a while loop.
number = int(input("Enter a number: "))
factor = 1
while factor <= number:
    if number % factor == 0:
        print(factor)
    factor += 1
# ============================================================
# WHILE LOOP - REVERSE A NUMBER
# ============================================================
# Example:
# 1234 -> 4321
# We take the last digit using % 10
# and build the reversed number.
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reversed number:", reverse)
# ============================================================
# WHILE LOOP - MULTIPLICATION TABLE
# ============================================================
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1
# Example input:
# 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50
# ============================================================
# WHILE LOOP - COUNTDOWN
# ============================================================
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Done!")
# ============================================================
# IMPORTANT OPERATORS USED WITH NUMBER LOOPS
# ============================================================
# %  -> Modulus
#      Gives the remainder.
# Example:
# 234 % 10 -> 4
# // -> Floor division
#      Gives the quotient without decimal part.
# Example:
# 234 // 10 -> 23
# ============================================================
# QUICK REVISION
# ============================================================
# while loop:
# -> Repeats code while a condition is True.
# break:
# -> Completely stops the loop.
# continue:
# -> Skips the current iteration.
# pass:
# -> Does nothing; used as a placeholder.
# range():
# -> Generates a sequence of numbers.
# %:
# -> Gives remainder.
# //:
# -> Gives integer quotient.
# max():
# -> Returns the largest value.
# ============================================================
# SIMPLE WAY TO REMEMBER
# ============================================================
# for
# -> "Go through these values."
# while
# -> "Keep going while this condition is True."
# break
# -> "STOP the loop."
# continue
# -> "SKIP this iteration."
# pass
# -> "DO NOTHING for now."