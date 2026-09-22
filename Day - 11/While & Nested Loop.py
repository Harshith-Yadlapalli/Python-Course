# ============================================================
# NESTED LOOPS IN PYTHON
# ============================================================
# A nested loop is a loop inside another loop.
# In simple words:
#     Outer loop -> controls the main/repeated process.
#     Inner loop -> runs completely for each iteration
#                   of the outer loop.
# Example:
# for i in range(3):
#     for j in range(3):
#         print(i, j)
# The inner loop runs 3 times for EVERY iteration
# of the outer loop.
# Total executions = 3 * 3 = 9
# ============================================================
# BASIC NESTED FOR LOOP
# ============================================================
for i in range(3):
    for j in range(3):
        print(i, j)
# Output:
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# ============================================================
# HOW A NESTED LOOP WORKS
# ============================================================
# Outer loop starts with i = 0.
# Then the inner loop runs completely:
# j = 0
# j = 1
# j = 2
# After that, outer loop changes i to 1.
# Again, inner loop runs completely:
# j = 0
# j = 1
# j = 2
# This continues until the outer loop finishes.
# ============================================================
# NESTED LOOP WITH A LIST
# ============================================================
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in numbers:
    for number in row:
        print(number)
# Output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# ============================================================
# PRINT EACH ROW
# ============================================================
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in numbers:
    print(row)
# Output:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# ============================================================
# MATRIX
# ============================================================
# A matrix can be represented using a nested list.
# Example:
#     1  2  3
#     4  5  6
#     7  8  9
# Here:
#     3 rows
#     3 columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# ============================================================
# ACCESSING MATRIX ELEMENTS USING INDEX
# ============================================================
# Matrix indexing:
# matrix[row][column]

# Example:
# matrix[0][0] -> 1
# matrix[0][1] -> 2
# matrix[0][2] -> 3

# matrix[1][0] -> 4
# matrix[1][1] -> 5
# matrix[1][2] -> 6

# matrix[2][0] -> 7
# matrix[2][1] -> 8
# matrix[2][2] -> 9
print(matrix[0][0])  # 1
print(matrix[0][1])  # 2
print(matrix[0][2])  # 3
print(matrix[1][0])  # 4
print(matrix[1][1])  # 5
print(matrix[1][2])  # 6
print(matrix[2][0])  # 7
print(matrix[2][1])  # 8
print(matrix[2][2])  # 9
# ============================================================
# PRINT MATRIX USING NESTED LOOPS
# ============================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in range(3):
    for column in range(3):
        print(matrix[row][column])
# ============================================================
# PRINT MATRIX IN ROW FORMAT
# ============================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in range(3):
    for column in range(3):
        print(matrix[row][column], end=" ")
    print()  # Move to the next line after each row
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
# ============================================================
# SAME MATRIX USING len()
# ============================================================
# Instead of hard-coding 3 rows and 3 columns,
# we can use len().
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end=" ")
    print()
# ============================================================
# NESTED LOOP WITH A 2D LIST
# ============================================================
# This is another common and simpler approach.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
# ============================================================
# NESTED WHILE LOOP
# ============================================================
# Nested loops can also be created using while loops.
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
# ============================================================
# EXAMPLE 1: PRINT A SQUARE PATTERN
# ============================================================
# We can use nested loops to create patterns.
#
# Here we want:
#
# * * *
# * * *
# * * *
for row in range(3):
    for column in range(3):
        print("*", end=" ")

    print()
# ============================================================
# EXAMPLE 2: PRINT A TRIANGLE PATTERN
# ============================================================
# Output:
#
# *
# * *
# * * *
# * * * *
for row in range(1, 5):
    for column in range(row):
        print("*", end=" ")
    print()
# ============================================================
# EXAMPLE 3: NUMBER PATTERN
# ============================================================
# Output:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
for row in range(1, 5):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
# ============================================================
# EXAMPLE 4: MULTIPLICATION TABLES
# ============================================================
# Nested loops can be used to print
# multiplication tables.
for number in range(1, 4):
    for multiplier in range(1, 11):
        print(number, "x", multiplier, "=", number * multiplier)
    print()  # Space between tables
# ============================================================
# EXAMPLE 5: FIND AN ELEMENT IN A MATRIX
# ============================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == target:
            print("Target found at:", row, column)
# Output:
# Target found at: 1 1
# ============================================================
# EXAMPLE 6: SUM OF ALL MATRIX ELEMENTS
# ============================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for row in matrix:
    for number in row:
        total += number
print("Sum:", total)
# Output:
# Sum: 45
# ============================================================
# EXAMPLE 7: FIND MAXIMUM IN A MATRIX
# ============================================================
matrix = [
    [1, 20, 3],
    [4, 5, 60],
    [7, 8, 9]
]
maximum = matrix[0][0]
for row in matrix:
    for number in row:
        if number > maximum:
            maximum = number
print("Maximum:", maximum)
# Output:
# Maximum: 60
# ============================================================
# IMPORTANT: NESTED LOOP STRUCTURE
# ============================================================
# Remember this structure:
# for row:
#     for column:
#         code

# The inner loop completes ALL its iterations
# before the outer loop moves to the next iteration.
# ============================================================
# LOOP VARIABLE MEANING
# ============================================================
# In a matrix:
# for row in range(len(matrix)):
#     -> row represents the row index.
# for column in range(len(matrix[row])):
#     -> column represents the column index.
# matrix[row][column]
#     -> accesses the value at that row and column.
# ============================================================
# NESTED LOOP - QUICK REVISION
# ============================================================
# Nested loop:
# -> A loop inside another loop.
# Outer loop:
# -> Controls the major/repeated operation.
# Inner loop:
# -> Runs completely for each iteration of the outer loop.
# Matrix:
# -> A common use case for nested loops.
# matrix[row][column]:
# -> Used to access a particular element in a matrix.
# end=" ":
# -> Keeps printing on the same line.
# print():
# -> Moves to the next line.
# ============================================================
# IMPORTANT CONCEPT
# ============================================================
# If the outer loop runs 3 times
# and the inner loop runs 4 times,
# total inner-loop executions = 3 * 4 = 12.
# Example:
# for i in range(3):
#     for j in range(4):
#         print(i, j)
# The print statement executes 12 times.