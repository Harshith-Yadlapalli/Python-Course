"""
PYTHON NESTED LOOPS & PATTERN PROGRAMS
---------------------------------------
A nested loop means a loop inside another loop.
Example:
for i in range(3):          # Outer loop
    for j in range(4):      # Inner loop
        print("*", end=" ")
    print()
The outer loop controls the rows.
The inner loop controls the columns/items in each row.
"""
# ============================================================
# 1. PRINT A RECTANGLE USING NESTED LOOPS
# ============================================================
# Outer loop -> controls the number of rows
for i in range(6):
    # Inner loop -> prints 4 stars in each row
    for j in range(4):
        print("*", end=" ")
    # Move to the next line after each row
    print()
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
# * * * *
# * * * *
# ============================================================
# 2. PRINT X PATTERN
# ============================================================
n = int(input("Enter the size: "))
for i in range(n):              # Controls rows
    for j in range(n):          # Controls columns
        # Print * on both diagonals
        if i == j or (i + j) == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Example for n = 5:
#
# *       *
#   *   *
#     *
#   *   *
# *       *
# ============================================================
# 3. PRINT PLUS (+) PATTERN
# ============================================================
n = 5
for row in range(1, n + 1):
    for col in range(n):
        # Middle row and middle column contain stars
        if row == n // 2 or col == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Output:
#     *
#     *
# * * * * *
#     *
#     *
# ============================================================
# 4. PRINT INCREASING NUMBERS USING NESTED LOOPS
# ============================================================
n = 1
# Outer loop controls rows
for row in range(3):
    # Inner loop controls columns
    for column in range(1):
        print(n, end=" ")
    # Increase the number after every row
    n = n + 1
    print()
# Output:
# 1
# 2
# 3
# ============================================================
# 5. PRINT CHECKERBOARD PATTERN
# ============================================================
n = int(input("Enter the size: "))
for row in range(n):
    for column in range(n):
        # Even sum -> 1, odd sum -> 0
        if (row + column) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
# Example for n = 5:
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# ============================================================
# 6. PRINT EVEN / ODD NUMBERS IN A PATTERN
# ============================================================
even = 2
odd = 1
for row in range(4):
    for column in range(4):
        # Check whether 2000 is even
        if 2000 % 2 == 0:
            print(even, end=" ")
            even += 2
        else:
            print(odd, end=" ")
            odd += 2
    print()
# Since 2000 is even, the output contains even numbers.
# 2 4 6 8
# 10 12 14 16
# 18 20 22 24
# 26 28 30 32
# ============================================================
# 7. RIGHT-ANGLE STAR TRIANGLE
# ============================================================
n = int(input("Enter the number of rows: "))
for row in range(1, n + 1):
    # Number of stars depends on the current row
    for column in range(row):
        print("*", end=" ")
    print()
# Example for n = 5:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# ============================================================
# 8. RIGHT-ANGLE TRIANGLE USING A CONDITION
# ============================================================
n = int(input("Enter the number of rows: "))
for row in range(n):
    for column in range(n):
        # Print stars only when column <= row
        if column <= row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Example for n = 5:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# ============================================================
# EXTRA EXAMPLE 1: BASIC FOR LOOP
# ============================================================
# A for loop repeats code for every value in a sequence.
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# ============================================================
# EXTRA EXAMPLE 2: FOR LOOP WITH A LIST
# ============================================================
numbers = [10, 20, 30, 40]
for number in numbers:
    print(number)
# Output:
# 10
# 20
# 30
# 40
# ============================================================
# EXTRA EXAMPLE 3: NESTED LOOP
# ============================================================
# Outer loop runs 3 times
for i in range(3):
    # Inner loop runs 2 times for every outer loop
    for j in range(2):
        print("i =", i, "j =", j)
# Output:
# i = 0 j = 0
# i = 0 j = 1
# i = 1 j = 0
# i = 1 j = 1
# i = 2 j = 0
# i = 2 j = 1
# ============================================================
# EXTRA EXAMPLE 4: MULTIPLICATION TABLE
# ============================================================
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# ============================================================
# EXTRA EXAMPLE 5: NESTED LOOP MULTIPLICATION TABLE
# ============================================================
# Prints tables from 1 to 3
for i in range(1, 4):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
# ============================================================
# EXTRA EXAMPLE 6: PRINT A SQUARE OF NUMBERS
# ============================================================
n = 4
for row in range(n):
    for column in range(n):
        print(column + 1, end=" ")
    print()
# Output:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# ============================================================
# EXTRA EXAMPLE 7: INVERTED STAR TRIANGLE
# ============================================================
n = 5
for row in range(n, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# ============================================================
# EXTRA EXAMPLE 8: BREAK IN A LOOP
# ============================================================
# break completely stops the loop.
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# ============================================================
# EXTRA EXAMPLE 9: CONTINUE IN A LOOP
# ============================================================
# continue skips the current iteration.
for i in range(6):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4
# 5