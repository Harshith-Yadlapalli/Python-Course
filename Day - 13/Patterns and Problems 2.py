"""
PATTERN PRINTING + ASCII + NESTED LOOPS
---------------------------------------
This file contains examples of:
1. Name pattern printing
2. Character/ASCII values
3. Character patterns using loops
4. Nested loops
5. Matrix diagonal subtraction
6. Extra loop examples
ASCII:
A = 65
B = 66
C = 67
Z = 90
chr() converts an ASCII number into a character.
Example: chr(65) -> 'A'
"""
# ============================================================
# 1. NAME PRINTING PATTERN
# ============================================================
name = "nayan"
# Print one more character of the name in every iteration
for p in range(len(name)):
    print(name[0:p + 1])
# Output:
# n
# na
# nay
# naya
# nayan
# ============================================================
# EXTRA EXAMPLE 1: REVERSE NAME PATTERN
# ============================================================
name = "nayan"
# Remove one character from the end in every iteration
for p in range(len(name), 0, -1):
    print(name[:p])
# Output:
# nayan
# naya
# nay
# na
# n
# ============================================================
# 2. REPEATING CHARACTERS USING STRING MULTIPLICATION
# ============================================================
name = "nayan"
# Repeat each character according to its position
for i in range(1, len(name) + 1):
    print(name[i - 1] * i)
# Output:
# n
# aa
# yyy
# aaaa
# nnnnn
# ============================================================
# EXTRA EXAMPLE 2: REPEAT EACH CHARACTER 3 TIMES
# ============================================================
name = "nayan"
# Print every character three times
for char in name:
    print(char * 3)
# Output:
# nnn
# aaa
# yyy
# aaa
# nnn
# ============================================================
# 3. ASCII VALUE -> CHARACTER
# ============================================================
ch = 65
# chr() converts an ASCII value into a character
print(chr(ch))
# Output:
# A
# ============================================================
# 4. ASCII VALUE 64
# ============================================================
ch = 64
# 64 represents the @ character in ASCII
print(chr(ch))
# Output:
# @
# ============================================================
# 5. PRINT ALPHABETS USING A FOR LOOP
# ============================================================
ch = 65
# Print A, B, C, D
for i in range(4):
    print(chr(ch), end=" ")
    # Move to the next ASCII value
    ch += 1
# Output:
# A B C D
# ============================================================
# EXTRA EXAMPLE 3: PRINT A TO Z
# ============================================================
ch = 65
# ASCII values of A to Z are 65 to 90
for i in range(26):
    print(chr(ch), end=" ")
    # Move to the next character
    ch += 1
# Output:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# ============================================================
# 6. ALPHABET PATTERN USING NESTED LOOPS
# ============================================================
ch = 65
# Outer loop controls rows
for row in range(4):
    # Inner loop controls columns
    for column in range(4):
        print(chr(ch), end=" ")
    # Move to the next character after every row
    ch += 1
    print()
# Output:
# A A A A
# B B B B
# C C C C
# D D D D
# ============================================================
# EXTRA EXAMPLE 4: CONTINUOUS ALPHABET PATTERN
# ============================================================
ch = 65
# Outer loop controls rows
for row in range(4):
    # Inner loop prints 4 characters
    for column in range(4):
        print(chr(ch), end=" ")
        # Move to the next character
        ch += 1
    print()
# Output:
# A B C D
# E F G H
# I J K L
# M N O P
# ============================================================
# 7. MATRIX - SUBTRACT TWO DIAGONALS
# ============================================================
"""
We have a square matrix.
Main diagonal:
        \
Other diagonal:
        /
We calculate:
diagonal_1 - diagonal_2
Then use abs() to get the absolute value.
"""
d1 = 0
d2 = 0
m = [
    [10, 20, 30, 40],
    [30, 60, 70, 80],
    [90, 100, 200, 300],
    [400, 500, 600, 700]
]
# Outer loop goes through rows
for r in range(len(m)):
    # Inner loop goes through columns
    for c in range(len(m[0])):
        # Main diagonal condition
        if r == c:
            d1 += m[r][c]
        # Other diagonal condition
        elif (r + c) == len(m) - 1:
            d2 += m[r][c]
print(d1, d2)
# Find the absolute difference between diagonals
print(abs(d1 - d2))
# Main diagonal:
# 10 + 60 + 200 + 700 = 970
# Other diagonal:
# 40 + 70 + 100 + 400 = 610
# Output:
# 970 610
# 360
# ============================================================
# EXTRA EXAMPLE 5: PRINT BOTH DIAGONALS
# ============================================================
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Print the main diagonal
print("Main diagonal:")
for i in range(len(m)):
    print(m[i][i], end=" ")
print()
# Print the other diagonal
print("Other diagonal:")
for i in range(len(m)):
    print(m[i][len(m) - 1 - i], end=" ")
# Output:
# Main diagonal:
# 1 5 9
# Other diagonal:
# 3 5 7
# ============================================================
# 8. BASIC FOR LOOP
# ============================================================
# range(5) generates 0, 1, 2, 3, 4
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# ============================================================
# 9. FOR LOOP WITH A STRING
# ============================================================
name = "Python"
# Loop through each character
for char in name:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n
# ============================================================
# 10. NESTED LOOP
# ============================================================
"""
A nested loop is a loop inside another loop.
Outer loop -> controls rows
Inner loop -> controls columns
"""
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()
# Output:
# * * * *
# * * * *
# * * * *
# ============================================================
# EXTRA EXAMPLE 6: NUMBER PATTERN USING NESTED LOOPS
# ============================================================
for row in range(1, 5):
    # Print numbers from 1 up to the current row
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ============================================================
# 11. STRING SLICING INSIDE A LOOP
# ============================================================
name = "nayan"
# Slicing gets characters from index 0 to i
for i in range(len(name)):
    print(name[:i + 1])
# Output:
# n
# na
# nay
# naya
# nayan
# ============================================================
# 12. STRING MULTIPLICATION
# ============================================================
name = "Python"
# * repeats a string
print(name * 2)
# Output:
# PythonPython
# ============================================================
# QUICK REVISION
# ============================================================
# len() -> returns length
name = "nayan"
print(len(name))                 # 5
# String slicing
print(name[:3])                  # nay
# String multiplication
print("A" * 5)                   # AAAAA
# chr() -> ASCII number to character
print(chr(65))                  # A
# ord() -> character to ASCII number
print(ord("A"))                 # 65
# Basic for loop
for i in range(5):
    print(i)
# Nested loop
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()