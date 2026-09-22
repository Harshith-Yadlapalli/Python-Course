""" Lists in Python
A list in Python is a collection used to store multiple items in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.
Lists are created using square brackets []. """ 

# Example:
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])
# Output:
# ['apple', 'banana', 'mango']
# apple

# ============================================================
# PYTHON LISTS
# ============================================================
# -------------------- LIST SLICING --------------------
l = [1, 2, 3]
print(l[1])       # Access the element at index 1
print(l[0:2])     # Get elements from index 0 to 1
print(l[1:])      # Get elements from index 1 till the end
print(l[::-1])    # Reverse the list using slicing
print(l[::2])     # Take every 2nd element
# -------------------- TAKING LIST INPUT --------------------
# Takes space-separated input and converts each value to an integer
l = list(map(int, input().split()))
print(l)
# ============================================================
# LIST CHARACTERISTICS
# ============================================================
# List is an ordered collection of data
# List is mutable
# List supports indexing
# List supports slicing
# ============================================================
# LIST METHODS
# ============================================================
# -------------------- 1. append() --------------------
l = []
l.append(10)          # Add 10 to the end of the list
l.append(20)          # Add 20 to the end of the list
print(l)              # [10, 20]
# -------------------- 2. extend() --------------------
l = [20, 60, 70]
l.extend([80, 90])    # Add multiple elements to the end of the list
print(l)              # [20, 60, 70, 80, 90]
# -------------------- 3. insert() --------------------
l = [20, 100]
l.insert(1, 30)        # Insert 30 at index 1
print(l)              # [20, 30, 100]
# -------------------- 4. pop() --------------------
l = [10, 20, 100, 30, 40, 50, 60, 70]
l.pop()               # Remove the last element
print(l)
l.pop(2)              # Remove the element at index 2
print(l)
# -------------------- 5. remove() --------------------
l = [10, 20, 100, 30, 40, 50, 60, 70]
l.remove(100)         # Remove the first occurrence of 100
print(l)
# -------------------- 6. sort() --------------------
l = [20, 5, 4, 1, 3]
l.sort()              # Sort the list in ascending order
print(l)              # [1, 3, 4, 5, 20]
l.sort(reverse=True)  # Sort the list in descending order
print(l)              # [20, 5, 4, 3, 1]
# -------------------- 7. count() --------------------
l = [1, 2, 2, 3, 2, 4]
print(l.count(2))     # Count how many times 2 occurs in the list
# -------------------- 8. index() --------------------
l = [10, 20, 30, 40, 50]
print(l.index(30))    # Find the index of 30
# -------------------- 9. reverse() --------------------
l = [1, 2, 3, 4, 5]
l.reverse()           # Reverse the list in-place
print(l)              # [5, 4, 3, 2, 1]
# -------------------- 10. copy() --------------------
l = [1, 2, 3, 4, 5]
new_l = l.copy()      # Create a copy of the list
print(new_l)
# ============================================================
# BUILT-IN FUNCTIONS USED WITH LISTS
# ============================================================
# -------------------- len() --------------------
l = [10, 20, 30, 40, 50]
print(len(l))         # Returns the number of elements in the list(length of list)
# -------------------- sum() --------------------
l = [10, 20, 30, 40, 50]
print(sum(l))         # Returns the sum of all elements
# -------------------- min() --------------------
l = [10, 20, 30, 40, 50]
print(min(l))         # Returns the smallest element
# -------------------- max() --------------------
l = [10, 20, 30, 40, 50]
print(max(l))         # Returns the largest element
# -------------------- sorted() --------------------
l = [5, 2, 4, 1, 3]
sorted_l = sorted(l)  # Creates a new sorted list
print(sorted_l)       # [1, 2, 3, 4, 5]
print(l)              # Original list remains unchanged

# List methods modify the original list (in many cases)
l.sort()
l.reverse()
l.append(10)
l.remove(10)
l.pop()
# sorted() creates and returns a new sorted list
new_l = sorted(l)

# List Slicing in Python
# List slicing is used to get a portion of a list. The basic syntax is:
# list[start:stop:step]
# start → index where slicing begins
# stop → index where slicing ends (not included)
# step → how many positions to move each time
# Example
numbers0 = [10, 20, 30, 40, 50, 60]
print(numbers0[1:4])
""" List Methods :-"""
# 1. append()
# 2. extend()
# 3. insert()
# 4. pop()
# 5. remove()
# 6. sort()
# 7. count()
# 8. index()
# 9. reverse()
# 10. copy()

"""Tuples in Python
A tuple is a collection used to store multiple values in a single variable. Tuples are similar to lists, but the main difference is that tuples are immutable, meaning their values cannot be changed after creation.
Tuples are created using parentheses ()."""

# Characteristics of Tuples
# Ordered – Elements maintain their order.
# Immutable – Elements cannot be changed, added, or removed after creation.
# Allow duplicates – The same value can appear multiple times.
# Can contain different data types – A tuple can contain strings, integers, floats, etc.
# Indexed – Elements can be accessed using their index, starting from 0.
# Can be sliced – You can extract a portion of a tuple using slicing.
# Faster than lists – Because tuples are immutable, they can generally be processed slightly faster than lists.
# Small Example
fruits1 = ("apple", "banana", "mango")
print(fruits1)
print(fruits1[1])
# Output:
# ('apple', 'banana', 'mango')
# banana

# METHODS :-
# count()
# t.count(10)
# index()
# sorted()
# sort()