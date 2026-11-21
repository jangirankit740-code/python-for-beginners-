
# ============================================================
# PYTHON FUNDAMENTALS FOR ABSOLUTE BEGINNERS
# Part 1: Output, Variables, Data Types, Input, and Comments
# ============================================================

# Welcome!
# Python is a programming language that allows us to
# give instructions to a computer.
#
# In this lesson, we will learn:
# 1. How to display messages using print()
# 2. How to store information using variables
# 3. How to identify different data types
# 4. How to receive information using input()
# 5. How to join strings using concatenation
# 6. How to write comments in Python


# ============================================================
# 1. OUTPUT - THE print() FUNCTION
# ============================================================

# The print() function displays information on the screen.
# We can use it to display text, numbers, and other values.

print("Hello there")
print("This is Ankit")

# Expected output:
# Hello there
# This is Ankit


# We can use either single quotes ('') or double quotes ("")
# when writing strings in Python.

print('Hello there')
print("Hello there")

# Both statements produce the same output.


# ------------------------------------------------------------
# Printing multiple values
# ------------------------------------------------------------

# We can display multiple values using a comma (,).
# Python automatically adds a space between them.

print("Hello there", "This is Ankit")

# Output:
# Hello there This is Ankit


# We can also write everything inside one string.

print("Hello there! This is Ankit")


# ------------------------------------------------------------
# Repeating strings using *
# ------------------------------------------------------------

# The * operator can repeat a string multiple times.

print("*" * 20)

# Output:
# ********************

# Explanation:
# "*" is a string containing one asterisk.
# 20 tells Python how many times to repeat it.


# ============================================================
# 2. VARIABLES - STORING INFORMATION
# ============================================================

# A variable is a name used to store a value.
#
# Imagine a variable as a labeled box.
# The label is the variable name.
# The contents of the box are the stored value.

name = "Ankit"
age = 27

# Here:
# name is a variable containing the string "Ankit".
# age is a variable containing the integer 27.

print(name)
print(age)

# Output:
# Ankit
# 27


# ------------------------------------------------------------
# Updating variables
# ------------------------------------------------------------

# We can change the value stored in a variable.

age = 28

print(age)

# Output:
# 28

# Important:
# The = symbol assigns a value to a variable.
# It does not mean mathematical equality.
#
# Python variable names are case-sensitive.
# For example, name and Name are different variables.
#
# By convention, Python variables use lowercase letters
# and underscores, such as first_name or user_age.


# ============================================================
# 3. DATA TYPES - UNDERSTANDING DIFFERENT VALUES
# ============================================================

# Every value in Python has a data type.
# A data type tells Python what kind of value it is.
#
# We will start with four common built-in data types:
#
# 1. str   = String (text)
# 2. int   = Integer (whole number)
# 3. float = Floating-point number (decimal number)
# 4. bool  = Boolean (True or False)


# ------------------------------------------------------------
# 3.1 STRING - str
# ------------------------------------------------------------

# A string represents text.
# Strings are written inside quotation marks.

name = "Ankit"
city = "Wroclaw"

print(type(name))

# Output:
# <class 'str'>


# ------------------------------------------------------------
# 3.2 INTEGER - int
# ------------------------------------------------------------

# Integers are whole numbers without decimal points.
# They can be positive, negative, or zero.

age = 27
temperature = -5

print(type(age))

# Output:
# <class 'int'>


# ------------------------------------------------------------
# 3.3 FLOAT - float
# ------------------------------------------------------------

# Floats represent numbers with decimal points.

height = 1.78
price = 11.50

print(type(height))

# Output:
# <class 'float'>


# ------------------------------------------------------------
# 3.4 BOOLEAN - bool
# ------------------------------------------------------------

# Boolean values represent two logical states:
# True or False.

is_student = True
is_employed = False

print(type(is_student))

# Output:
# <class 'bool'>

# IMPORTANT:
# Python is case-sensitive.
# Boolean values must be written as True or False.
# Writing true or false will cause an error unless
# you have defined variables with those names.


# ------------------------------------------------------------
# Checking multiple data types
# ------------------------------------------------------------

name = "Ankit"
age = 27
height = 1.78
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

# The type() function tells us the data type of a value.


# ============================================================
# 4. INPUT - RECEIVING INFORMATION FROM USERS
# ============================================================

# The input() function allows users to enter information.
#
# When Python reaches input(), the program pauses
# and waits for the user to type something.
#
# The user presses Enter to submit their response.


# ------------------------------------------------------------
# Example 1: Input without storing the result
# ------------------------------------------------------------

input("Enter your name: ")

# This displays a question and accepts an answer.
# However, the answer is not saved in a variable.


# ------------------------------------------------------------
# Example 2: Input stored in a variable
# ------------------------------------------------------------

name = input("Enter your name: ")

print(name)

# Example:
# Enter your name: Ankit
# Ankit

# Explanation:
# 1. Python displays "Enter your name:"
# 2. The user types Ankit.
# 3. Python stores "Ankit" in the variable name.
# 4. print(name) displays the stored value.


# ------------------------------------------------------------
# IMPORTANT: input() always returns a string
# ------------------------------------------------------------

age = input("Enter your age: ")

print(type(age))

# Example input: 27
#
# Output:
# <class 'str'>

# Even though the user entered 27, Python stores it
# as a string because input() always returns text.


# ------------------------------------------------------------
# Converting input into an integer
# ------------------------------------------------------------

age = int(input("Enter your age: "))

print(type(age))

# Example input: 27
#
# Output:
# <class 'int'>

# int() converts a valid whole-number string into an integer.
# If the user enters text such as "hello", this will fail.


# ============================================================
# 5. CONCATENATION - JOINING STRINGS
# ============================================================

# Concatenation means joining strings together.
#
# We can use the + operator to combine strings.

first_name = "Ankit"
last_name = "Jangir"

full_name = first_name + " " + last_name

print(full_name)

# Output:
# Ankit Jangir

# Explanation:
# first_name contains "Ankit".
# " " adds a space between the names.
# last_name contains "Jangir".
# The + operator joins these strings.


# ------------------------------------------------------------
# Concatenation with user input
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Hello " + name)

# Example:
# Enter your name: Ankit
# Hello Ankit


# ------------------------------------------------------------
# Difference between commas and concatenation
# ------------------------------------------------------------

print("Hello", name)
print("Hello " + name)

# Both display:
# Hello Ankit

# Difference:
# A comma lets print() display multiple values.
# By default, print() adds a space between them.
#
# The + operator joins strings into one string.
# We must add spaces ourselves when using +.


# ------------------------------------------------------------
# Common beginner mistake
# ------------------------------------------------------------

age = 27

# This will cause a TypeError:
# print("My age is " + age)

# Why?
# Because "My age is " is a string,
# but age is an integer.
# Python cannot directly concatenate these two types.


# Solution 1: Convert the integer into a string.

print("My age is " + str(age))

# Solution 2: Use a comma.

print("My age is", age)

# Solution 3: Use an f-string.

print(f"My age is {age}")

# Output for all three:
# My age is 27

# f-strings allow us to insert variables into strings.
# We will explore them in more detail in a future lesson.


# ============================================================
# 6. COMMENTS - EXPLAINING YOUR CODE
# ============================================================

# Comments are notes written inside Python code.
# They help people understand what the code does.
#
# Python ignores comments when running the program.
#
# A single-line comment begins with #.

# This is a comment.

print("Python is fun!")  # This is an inline comment.

# Comments are useful for:
# - Explaining difficult code
# - Documenting important information
# - Making programs easier to understand
# - Temporarily disabling a line of code


# ============================================================
# 7. MINI PROJECT - PERSONAL INTRODUCTION
# ============================================================

# Let's combine what we have learned.

print("=" * 40)
print("WELCOME TO MY FIRST PYTHON PROGRAM")
print("=" * 40)

name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Which city do you live in? ")

print()
print("----- YOUR INTRODUCTION -----")

print(f"Hello, my name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")

print("-----------------------------")

# Example output:
#
# What is your name? Ankit
# How old are you? 27
# Which city do you live in? Wroclaw
#
# ----- YOUR INTRODUCTION -----
# Hello, my name is Ankit.
# I am 27 years old.
# I live in Wroclaw.
# -----------------------------


# ============================================================
# END OF PART 1
# ============================================================

# Congratulations!
#
# You have learned:
# - print() for displaying information
# - Variables for storing values
# - str, int, float, and bool data types
# - type() for checking data types
# - input() for receiving user information
# - Concatenation using +
# - Type conversion using int() and str()
# - f-strings for displaying variables
# - Comments for explaining code
#
# NEXT LESSON:
# Part 2 - Operators and Basic Calculations
