# ============================================================
# PYTHON SETS, DICTIONARIES
# ============================================================
# 1. SETS
# ============================================================
# A set is an unordered collection of data.
# A set stores only unique elements.
# A set is mutable.
# Sets do not support indexing because they are unordered.
s = {1, 4, 5}
print(s)
# Duplicate elements are automatically removed.
s = {1, 2, 2, 3, 3, 4}
print(s)              # {1, 2, 3, 4}
# ------------------------------------------------------------
# EMPTY SET
# ------------------------------------------------------------
# IMPORTANT:
# {} creates an empty DICTIONARY, not an empty set.
empty_dict = {}
# To create an empty set, use set().
empty_set = set()
print(type(empty_dict))   # <class 'dict'>
print(type(empty_set))    # <class 'set'>
# ============================================================
# SET OPERATIONS
# ============================================================
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# -------------------- 1. UNION --------------------
# Union combines all unique elements from both sets.
print(s1.union(s2))
# Output:
# {1, 2, 3, 4, 5, 6}
# The | operator can also be used for union.
print(s1 | s2)
# Output:
# {1, 2, 3, 4, 5, 6}
# -------------------- 2. INTERSECTION --------------------
# Intersection returns the common elements.
print(s1.intersection(s2))
# Output:
# {3, 4}
# The & operator can also be used.
print(s1 & s2)
# Output:
# {3, 4}
# -------------------- 3. DIFFERENCE --------------------
# s1 - s2 gives elements present in s1 but NOT in s2.
print(s1.difference(s2))
# Output:
# {1, 2}
# s2 - s1 gives elements present in s2 but NOT in s1.
print(s2 - s1)
# Output:
# {5, 6}
# -------------------- 4. SYMMETRIC DIFFERENCE --------------------
# Returns elements that are in either set,
# but NOT in both sets.
print(s1.symmetric_difference(s2))
# Output:
# {1, 2, 5, 6}
# The ^ operator can also be used.
print(s1 ^ s2)
# Output:
# {1, 2, 5, 6}
# -------------------- 5. ISSUBSET --------------------
# A set is a subset if all its elements are present
# inside another set.
s1 = {1, 2, 3, 4}
s2 = {4}
print(s2.issubset(s1))
# Output:
# True
# Another example:
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))      # True
print(b.issubset(a))      # False
# ============================================================
# SET METHODS
# ============================================================
s1 = {1, 2, 3, 4}
# -------------------- 1. add() --------------------
# Adds one element to the set.
s1.add(5)
print(s1)
# Output:
# {1, 2, 3, 4, 5}
# -------------------- 2. update() --------------------
# Adds multiple elements to the set.
s1.update([6, 7, 8])
print(s1)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}
# -------------------- 3. remove() --------------------
# Removes a specific element.
# Gives a KeyError if the element does not exist.
s1.remove(8)
print(s1)
# Example:
s = {1, 2, 3}
# s.remove(10)       # KeyError because 10 does not exist
# -------------------- 4. discard() --------------------
# Removes an element if it exists.
# Unlike remove(), discard() does NOT give an error
# if the element does not exist.
s = {1, 2, 3}
s.discard(10)
print(s)             # {1, 2, 3}
# -------------------- 5. pop() --------------------
# Removes and returns an arbitrary element from a set.
s = {10, 20, 30}
removed = s.pop()
print(removed)
print(s)
# -------------------- 6. clear() --------------------
# Removes all elements from the set.
s = {1, 2, 3}
s.clear()
print(s)             # set()
# -------------------- 7. del -------------------
# del removes the entire set variable.
s = {1, 2, 3}
del s
# print(s)           # NameError because s no longer exists
# ============================================================
# 3. REMOVE DUPLICATES USING SET
# ============================================================
# A set automatically removes duplicate values.
l = [1, 2, 3, 4, 10, 40, 4, 2, 1]
s = set(l)
print(s)
# Possible output:
# {1, 2, 3, 4, 10, 40}
# IMPORTANT:
# Converting a list to a set removes duplicates,
# but it does not preserve the original list order.
# If you need unique values while preserving order:
l = [1, 2, 3, 4, 10, 40, 4, 2, 1]
unique_values = list(dict.fromkeys(l))
print(unique_values)
# Output:
# [1, 2, 3, 4, 10, 40]
# ============================================================
# 4. DICTIONARY
# ============================================================
# A dictionary stores data in KEY : VALUE pairs.
# A dictionary is mutable.
# Keys must be unique.
# Values can be duplicated.
# Dictionaries are ordered by insertion order in modern Python.
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(d)
# Accessing a value using its key.
print(d["a"])
# Output:
# 1
# Another example:
student = {
    "name": "Nayan",
    "age": 22,
    "course": "Python"
}
print(student["name"])
print(student["age"])
# ============================================================
# DICTIONARY MAPPING
# ============================================================
# Dictionary maps a key to a value.
#       KEY       VALUE
#        a          1
#        b          2
#        c          3
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
# ------------------------------------------------------------
# DICTIONARY KEYS MUST BE UNIQUE
# ------------------------------------------------------------
# If duplicate keys are used, the latest value replaces
# the previous value.
d = {
    "a": 1,
    "b": 2,
    "a": 4
}
print(d)
# Output:
# {'a': 4, 'b': 2}
# ============================================================
# DICTIONARY METHODS
# ============================================================
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
# -------------------- 1. keys() --------------------
# Returns all keys.
print(d.keys())
# Output:
# dict_keys(['a', 'b', 'c'])
# -------------------- 2. values() --------------------
# Returns all values.
print(d.values())
# Output:
# dict_values([1, 2, 3])
# -------------------- 3. items() --------------------
# Returns all key-value pairs.
print(d.items())
# Output:
# dict_items([('a', 1), ('b', 2), ('c', 3)])
# -------------------- 4. update() --------------------
# Adds new key-value pairs or updates existing keys.
d.update({"d": 4})
print(d)
# Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Updating an existing key:
d.update({"a": 100})
print(d)
# 'a' is updated from 1 to 100.
# -------------------- 5. pop() --------------------
# Removes the specified key and returns its value.
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
value = d.pop("b")
print(value)         # 2
print(d)             # {'a': 1, 'c': 3}
# -------------------- 6. popitem() --------------------
# Removes and returns the last inserted key-value pair.
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
item = d.popitem()
print(item)          # ('c', 3)
print(d)             # {'a': 1, 'b': 2}
# -------------------- 7. get() --------------------
# get() safely retrieves a value using a key.
d = {
    "name": "Nayan",
    "age": 22
}
print(d.get("name"))     # Nayan
print(d.get("age"))      # 22
# If the key doesn't exist, get() returns None
# instead of raising a KeyError.
print(d.get("city"))     # None
# We can provide a default value.
print(d.get("city", "Not Found"))
# Output:
# Not Found
# ============================================================
# 5. PACKING AND UNPACKING
# ============================================================
# -------------------- PACKING --------------------
# Packing means putting multiple values into one tuple.
t = 1, 2, 3, 4
print(t)
# Output:
# (1, 2, 3, 4)
# You can also explicitly use parentheses.
t = (1, 2, 3, 4)
print(t)
# -------------------- UNPACKING --------------------
# Unpacking means taking values from a tuple
# and assigning them to separate variables.
t = (1, 2, 3, 4)
a, b, c, d = t
print(a)              # 1
print(b)              # 2
print(c)              # 3
print(d)              # 4
# The number of variables must normally match
# the number of values.
t = (1, 2, 3)
# a, b = t            # ValueError
# ============================================================
# 6. STAR (*) UNPACKING
# ============================================================
# * can collect multiple remaining values into a list.
t = (1, 2, 3, 4)
a, *b = t
print(a)              # 1
print(b)              # [2, 3, 4]
# Another example:
t = (1, 2, 3, 4)
*a, b = t
print(a)              # [1, 2, 3]
print(b)              # 4
# The * variable collects the remaining values.
# ============================================================
# 7. NUMBER SYSTEM / BINARY
# ============================================================
# Computers internally work with binary numbers.
# Binary uses only two digits: 0 and 1.
# Decimal 4 in binary:
# 4 -> 100
# Decimal 3 in binary:
# 3 -> 011
# Decimal 2 in binary:
# 2 -> 010
# Decimal 1 in binary:
# 1 -> 001
# ============================================================
# DECIMAL TO BINARY
# ===========================================================
# bin() converts a decimal integer into binary.
print(bin(4))
# Output:
# 0b100
# "0b" tells Python that the number is binary.
print(bin(10))
# Output:
# 0b1010
# ============================================================
# BINARY TO DECIMAL
# ============================================================
# int(binary_number, 2) converts binary to decimal.
print(int("100", 2))
# Output:
# 4
print(int("1010", 2))
# Output:
# 10
# Another example:
binary = "1011"
decimal = int(binary, 2)
print(decimal)
# Output:
# 11
# ============================================================
# QUICK REVISION
# ============================================================
# TUPLE
# - Ordered
# - Immutable
# - Allows duplicates
# - Supports indexing
# - Main methods: count(), index()

# SET
# - Unordered collection
# - Mutable
# - Only unique elements
# - No indexing
# - Useful for set operations and removing duplicates

# DICTIONARY
# - Stores KEY : VALUE pairs
# - Mutable
# - Keys must be unique
# - Values can be duplicated
# - Useful for mapping data

# SET OPERATIONS
# union()                  -> Combine both sets
# intersection()           -> Common elements
# difference()             -> Elements present in one set only
# symmetric_difference()   -> Elements present in either set, but not both
# issubset()               -> Checks whether one set is inside another

# IMPORTANT SYMBOLS
# |  -> Union
# &  -> Intersection
# -  -> Difference
# ^  -> Symmetric Difference
# ============================================================
# METHOD VS FUNCTION
# ============================================================
# A method is called using the object.
# s.add(10)                  # Method
# d.keys()                   # Method
# t.count(10)                # Method
# # A built-in function is called directly.
# len(t)                     # Function
# sorted(t)                  # Function
# bin(10)                    # Function
# int("101", 2)              # Function