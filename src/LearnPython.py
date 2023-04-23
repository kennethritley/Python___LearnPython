'''
This file contains code snippets that demonstrate
all of the most commonly used SCRIPT functionality in Python.  Python
naturally offers classes and OO functionality, but here the focus
is on scripting, which is a good approach for BI dashboards and
quick-and-dirty tasks.

Author: KEN
Date:   2022.04.04
'''

#--------------------------------------------------------------------
# Datatypes do not need to be explicity declared
#--------------------------------------------------------------------

# Integers and floating points

myint = 7
myfloat = 7.0
myfloat = float(7)

# Extra for experts: Python uses "variable reassignment" and
# integers, floats, strings (and tuples, frozensets, etc.) are "immutable". This means
# if you do "a = 1" then an object is created and assigned to 1.
# If you do "a = a + 1" a new object is created and assigned 2, but the old object with
# the value of 1 exists in a unreferenced state until it is garbage collected!

# Example of traditional printing

print("\n----- Test of traditional printing")
print("This is an integer", myint)
print("Embedding an integer %d and a float %f in an output string" % (myint, myfloat)) # careful, %d is for ints
print("Here is an int and a float", myint, myfloat)

# Strings can use single or double quotes

mystring = 'hello'
mystring = "Ken's string"
print("\n----- Test of formatted printing")
print ("String:", mystring)
print ("String %s is embedded" % mystring) #careful, % operator needed for strings
print ("Length of string", len(mystring))
print ("First occurance of 'st'", mystring.index("st"))
print ("Substring", mystring[0:3]) # not what you'd expect
print ("Frequency of s", mystring.count("s"))

# Example of f-string printing - very cool and easy to use!

print("\n----- Test of f-printing")
print(f"This is an integer {myint} and this is a character string {mystring} ")

# Super powerful formatting with colors and escape sequences

print("\n----- Test of formatted printing")
print("\033[0;37;40m Normal text")
print("\033[2;37;40m Underlined text\033[0;37;40m ")
print("\033[1;37;40m Bright Colour\033[0;37;40m ")
print("\033[3;37;40m Negative Colour\033[0;37;40m ")
print("\033[5;37;40m Negative Colour\033[0;37;40m")

print("\n----- Test of colored printing")
print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")


# Printing ASCII 7 (BEL) will ring the bell, but it works better
# if you use time.sleep(1) after each call
print("\n----- This can ring the bell")
print("\x07",end="",flush=True)
print("\x07",end="",flush=True)
print("\x07",end="",flush=True)
print("\x07",end="",flush=True)
print("\x07",end="",flush=True)

#--------------------------------------------------------------------
# Conditionals
#--------------------------------------------------------------------
print("\n----- Test conditional")

# (1) EXAMPLE: Getting keyboard input
# (2) EXAMAPLE: Conditionals, if, elif, else. Note ":"
# (3) EXAMPLE: Multiline functionality uses an indent, 4 spaces is recommended

myint = int(input("Please enter a number:")) # input returns string so must be wrapped in int()

if myint == 1:
    print ("myint == 1", myint)
elif myint ==2:
    print ("myint >= 2", myint)
else:
    print ("myint was not 1 nor 2", myint)


#--------------------------------------------------------------------
# FOR Looping
#--------------------------------------------------------------------
print("\n----- FOR looping")

# For loop, see ":"

print("\n----- for looping over a RANGE")
for x in range(3):
    print("range[3], X=",x)
for x in range (2,5):
    print(" range[2,5] X=",x)
for x in range (3,8,2):
    print("range[3,7,2]X=",x)

print("\n----- for looping over a DICTIONARY")
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Iterating over keys
for key in person:
    print(key)

# Iterating over values
for value in person.values():
    print(value)

# Iterating over both keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# LOOP OVER A STRING

print("\n----- for looping over a STRING")
word = "hello"
for letter in word:
    print(letter)

# LOOP OVER A LIST

print("\n----- for looping over a LIST")
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)

# LOOP OVER A SET

print("\n----- for looping over a SET")
unique_numbers = {1, 2, 3, 4, 5} 
for number in unique_numbers:
    print(number)

#--------------------------------------------------------------------
# WHILE Looping
#--------------------------------------------------------------------
print("\n----- WHILE looping")

x=0
print("\n----- simple while looping")
while x<5:
    print ("While x==",x)
    x += 1

# Python's version of a Do loop

print("\n----- how to handle a do loop in Python")
x=0
while True:
    x = x+1
    if (x==5):
        print("Do End! X==",x)
        break
    print ("Do x==",x)

# Else with While loop - not many languages support this

print("\n----- while with else")
x=0
while x<5:
    print ("While with else x==",x)
    x += 1
else:
    print("Limit reached", x)

# Break

print("\n----- while with break")
x=0
while x<10:
    print ("While with break x==",x)
    x += 1
    if (x==4):
        print("X==4")
        break
    print("X==",x)

# Continue

print("\n----- while with continue")
x=0
while x<10:
    print ("While with continue x==",x)
    x += 1
    if (x==4):
        print("X==4 but we keep looping")
        continue
    print("X==",x)

#--------------------------------------------------------------------
# Arrays
#--------------------------------------------------------------------

# Python does not support arrays. Use lists instead or e.g. numpy

#--------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------
print("\n----- different function tests")

# Be careful. Variables in a function stay inside a function (local scope).
# A function also has access to all variables declared outside a function (global scope)

def myfunction1():
    myterm = 1.0 # has local scope, not known outside the function
    myanswer = 1.14 + myglobal # myglobal has global scope, can be used here
    return myanswer

myglobal = 2.0 # has global scope, can be used by function
myresult = myfunction1()
print ("The result from myfunction1 is ", myresult)

# With parameters

def myfunction2(myparam):
    myanswer = 1.14 + myparam # myanswer has global scope, can be used here
    return myanswer

myval = 2.0 # has global scope, can be used by function
myresult = myfunction2(myval)
print ("The result from myfunction2 is ", myresult)

# With parameters

def myfunction3(myparam):
    myanswer = 1.14 + myparam # myanswer has global scope, can be used here
    myparam = 100 # here we try to change the input parameter; the new value will NOT be passed back!
    return myanswer

myval = 2.0 # has global scope, can be used by function
myresult = myfunction3(myval)
print (f"The result from myfunction3 is {myresult}, the parameter was NOT changed {myval}")

#--------------------------------------------------------------------
# Advanced topics: lists, can be mixtures of different data types
#--------------------------------------------------------------------
print("\n----- advanced lists")

mylist1 = [] # empty list
mylist1.append(1) # add an integer
mylist1.append("apple") # add a string
mylist1.append(3.1415) # add a float
print("This is my list", mylist1)

mylist2 = [2, "banana", 2.718]
print("This is my list", mylist2)

mylist3 = [55,44,33,22,11]
i=0
while i < len(mylist3):
    print("list contains: ",mylist3[i])
    i=i+1

mylist4 = mylist3.copy() # How to copy a list
mylist4.sort() # how to sort a list
i=0
while i < len(mylist4):
    print("list contains: ",mylist4[i])
    i=i+1


#--------------------------------------------------------------------
# Advanced topics: dictionaries (pairs of tokens:values, but no order)
#--------------------------------------------------------------------
print("\n----- dictionaries")

mydict1 = {} # curly braces to say we have a list
mydict1["Ken"] = 1
mydict1["Kenny"] = 3.1415
mydict1["Kenneth"] = "Banjo"
print("My dictionary", mydict1)

mydict2 = {} # curly braces to say we have a list
mydict2 = { 
    "key_test_int" : 2,
    "key_test_float" : 2.718,
    "key_test_string" : "Yacht"
}
print("My dictionary", mydict2)

# Shows how to iterate through a dictionary
for mykey in mydict2:
    print("Key: ", mykey, mydict2[mykey])

# Shows a list where tokens are integers and values are lists
mydict3 = {} # curly braces to say we have a list
mydict3 = { 1 : [1,2,3], 2 : [3,4,5], 3 : [6,7,8], 4 : [9,10,11] }
print("My dictionary", mydict3)
del mydict3[1] # delete the token 1
mydict3.pop(2) # delete the token 2 by a different technique
print("My dictionary", mydict3)

# It's useful to create a new data structure that is just the values without the keys
# and now how to iterate through just the keys or just the values
myitems = mydict3.items()
for mykey, myvalue in myitems:
    print(mykey, "-->", myvalue)
myvalues = mydict3.values()
for myvalue in myvalues:
    print("Value:", myvalue)

#--------------------------------------------------------------------
# Python's version of Javadoc: Python docstrings. Note: the triple
# quotes you see here are comments but traditionally only used for 
# declarations and esp. Python docstrings. therwise use hash for comments
#--------------------------------------------------------------------
print("\n----- Python docstrings")

# Example in reStructuredText (reST) format
def add_reST(a, b):
    """
    Adds two numbers and returns the result.

    :param a: The first number to be added.
    :type a: int or float
    :param b: The second number to be added.
    :type b: int or float
    :return: The sum of a and b.
    :rtype: int or float
    """
    return a + b

# Example in Google format
def add_Google(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

print("\n----- Python docstrings reST format")
print(add_reST.__doc__)
print("\n----- Python docstrings Google format")
print(add_Google.__doc__)

print("all done.") # This is how the first supercomputers always ended applications

#--------------------------------------------------------------------
# These are the PEP8 style guide rules for formatting Python code
# https://peps.python.org/pep-0008/
#--------------------------------------------------------------------

# 1. Modules (Python files): Use lowercase names, and separate words with underscores if necessary (e.g., my_module.py).
#    Avoid using special characters or dashes.
#
# 2. Packages (directories containing an __init__.py file): Use lowercase names and avoid using underscores if possible (e.g., mypackage).
#
# 3. Functions and method names: Use lowercase names and separate words with underscores (e.g., my_function()).
#
# 4. Variables and instance variables: Use lowercase names and separate words with underscores (e.g., my_variable).
#
# 5. Constants: Use uppercase names and separate words with underscores (e.g., MY_CONSTANT).
#
# 6. Class names: Use the PascalCase (also known as CamelCase or UpperCamelCase) convention,
#    where each word in the name starts with an uppercase letter, and there are no underscores between words (e.g., MyClass).
#
# 7. Instance methods and class methods: Use lowercase names and separate words with underscores
#    (e.g., my_instance_method(self) or my_class_method(cls)).
#
# 8. Private methods and attributes: Prefix the name with an underscore (e.g., _my_private_method(self) or _my_private_attribute).

