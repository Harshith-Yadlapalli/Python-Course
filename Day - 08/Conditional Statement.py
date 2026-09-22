# ============================================================
# CONDITIONAL STATEMENTS IN PYTHON
# ============================================================

# Conditional statements are used to make decisions in a program.
#
# There are 4 main types:
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. nested if
# ============================================================
# 1. IF STATEMENT
# ============================================================
# The if statement executes a block of code
# only when the condition is True.

# Syntax:
# if condition:
#     statement

# Example:
age = 20
if age >= 18:
    print("You are eligible for voting")
# Another example:
number = 10
if number > 0:
    print("Number is positive")
# If the condition is False, the code inside if
# will not execute.
# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================
# if-else is used when we have two possible outcomes.
# If the condition is True -> if block executes.
# If the condition is False -> else block executes.

# Syntax:
#
# if condition:
#     statements
# else:
#     statements

# Example:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
# Another example:
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# ============================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================
# elif means "else if".
# It is used when we have multiple conditions.
# Python checks the conditions from top to bottom.
# The first True condition gets executed.
# Syntax:
# if condition1:
#     statements
# elif condition2:
#     statements
# elif condition3:
#     statements
# else:
#     statements
# Example: Grade calculation
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 35:
    print("D")
else:
    print("Fail")
# Another example:
temperature = 30
if temperature >= 40:
    print("Very hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Normal")
else:
    print("Cold")
# ============================================================
# 4. NESTED IF STATEMENT
# ============================================================
# A nested if means an if statement inside another if statement.
# The inner if is checked only when the outer if condition
# is True.
# Syntax:
# if condition1:
#     if condition2:
#         statements
#     else:
#         statements
# else:
#     statements
# Example:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("a is the greatest")
    else:
        print("c is the greatest")
else:
    if b > c:
        print("b is the greatest")
    else:
        print("c is the greatest")
# ============================================================
# QUICK EXAMPLE OF NESTED IF
# ============================================================
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID is required")
else:
    print("You are underage")
# ============================================================
# IMPORTANT NOTES
# ============================================================
# 1. Python uses indentation to define a block.
# 2. A colon (:) is required after if, elif and else.
# 3. Conditions usually use comparison operators:
#    >    greater than
#    <    less than
#    >=   greater than or equal to
#    <=   less than or equal to
#    ==   equal to
#    !=   not equal to
# 4. Logical operators can also be used:
#    and
#    or
#    not
# ============================================================
# LOGICAL OPERATORS WITH CONDITIONS
# ============================================================
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")
# ============================================================
# CONDITIONAL STATEMENTS - QUICK REVISION
# ============================================================
# 1. if
#    -> Used to check one condition.
# 2. if-else
#    -> Used when there are two possible outcomes.
# 3. if-elif-else
#    -> Used when there are multiple conditions.
# 4. nested if
#    -> An if statement inside another if statement.
# ============================================================
# PRACTICE EXAMPLES
# ============================================================
# Example 1: Check positive number
number = 10
if number > 0:
    print("Positive")

# Example 2: Check even or odd
number = 15
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 3: Check pass or fail
marks = 65
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Example 4: Grade using elif
marks = 82
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 35:
    print("D")
else:
    print("Fail")

# Example 5: Nested if
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Citizenship required")
else:
    print("Not eligible due to age")
# ============================================================
# SIMPLE WAY TO REMEMBER
# ============================================================
# if
# -> "If this is true, do this."
# if-else
# -> "If this is true, do this; otherwise do that."
# if-elif-else
# -> "Check multiple conditions one by one."
# nested if
# -> "Check another condition inside a condition."