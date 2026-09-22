# In Python, a string (str) is text—a sequence of characters.

name = "Alice"
message = 'Hello, world!'
print(name,message)


# F-string in Python
# An f-string is a way to easily put variables or expressions inside a string.
# You write an f before the string and put variables inside {}.

# Example:
name1 = "Nayan"
age1 = 22
print(f"My name is {name1} and I am {age1} years old.")

""" String Methods :- """
"""
1. Changing case
Method	                            What it does	                       Example
.upper()	                    Converts to uppercase	            "hello".upper() → "HELLO"
.lower()	                    Converts to lowercase	            "HELLO".lower() → "hello"
.capitalize()	                Capitalizes first character	        "hello world".capitalize() → "Hello world"
.title()	                    Capitalizes every word	            "hello world".title() → "Hello World"
.swapcase()	                    Swaps uppercase ↔ lowercase	        "HeLLo".swapcase() → "hEllO"
.casefold()	                    Stronger lowercase conversion	    "HELLO".casefold() → "hello"
"""

name2 = "nayan123"
print(name2.isupper())
print(name2.islower())
print(name2.isalnum())
print(name2.isalpha())
print(name2.isdigit())
print(name2.isspace())

# 4. Removing spaces/characters
text = "   Hello World   "
# # Method	        What it does	            Example
# .strip()	        Removes from both ends	    " hello ".strip() → "hello"
# .lstrip()	        Removes from left	        " hello".lstrip() → "hello"
# .rstrip()	        Removes from right	        "hello ".rstrip() → "hello"

# 5. Replacing
# .replace() replaces one part of a string with another.
text1 = "I like Java"
print(text1.replace("Java", "Python"))

# 6. Splitting strings
# .split() breaks a string into a list.
text2 = "apple banana mango"
print(text2.split())
 # Output:
# ['apple', 'banana', 'mango']

# 7. Joining strings
# .join() combines elements into one string.
words = ["I", "love", "Python"]
print(" ".join(words))
# Output:
# I love Python

""" String Operations :- """

""" 1. Concatenation + """
# Joining two or more strings.
a="hello"
b="python"
print(a + " " + b)
# Output:
# hello python

# 2. Comparing strings
# You can use comparison operators:
a1 = "apple"
b1 = "banana"
print(a1 == b1)
print(a1 != b1)
# Output:
# False
# True

# 3. Indexing []
# Accessing individual characters.
text4 = "Python"
print(text4[0])
print(text4[2])
print(text4[-1])
# Output:
# P
# t
# n

# 4. Slicing [:]
# Getting a portion of a string.
text = "Python"
print(text[0:3])
# Output:
# Pyt

# 5. Reverse a string
# Using slicing:
text5 = "Python"
print(text5[::-1])
# Output:
# nohtyP

# 6. String formatting with f-strings
# A cleaner way to put variables into strings:
name9 = "Nayan"
age9 = 22
print(f"My name is {name9} and I am {age9} years old.")