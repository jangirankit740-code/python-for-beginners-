# Python Programming 
# Part 2 

# 1type conversion/casting
# 2sum programme
# 3string methods
# 4keywords 
# All the input values are stored as str irrespective of any value which is stored init



Age = input ("Enter Your age: ")
print ( Age, type(Age))

#OUTPUT

# Enter Your age: 20
# 20 <class 'str'>

# print (Age + 1)
# TypeError: can only concatenate str (not "int") to str

# resean as follow

# here we can see that age is 20 and numbers are always int 
# but when we use input function it will alwasy create str value, irrespective of any value which is stored init

new_Age = int (Age) + 1
print (new_Age)

#OUTPUT

# Enter Your age: 20
# 20 <class 'str'>
# 21

print (float (new_Age)) 
#OUTPUT 
  # 21.0
print (1+3.98) 
# **Type Conversion (Implicit):** Handled automatically by Python (e.g., `1 + 3.98` produces `4.98`).

print (1 + int (3.98)  ) 

# * **Type Casting (Explicit):** Explicitly converted by programmer (e.g., `int(3.98)` produces `4`).


