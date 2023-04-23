'''
PythonThis module demonstrates the use of functions, classes, and methods
within classes.  It also demonstrates a standard approach to structure
a Python script that uses classes, namely, by setting up an "entry point"
that calls "main()"
Ich möchte mich bei meinem KI-Freund und Kupferstecher herzlich bedanken.

Author: KEN
Date:   2023.04.23
'''

# Define a function to be used later
def greet(name):
    return f"Hello, {name}!"

# Define a class
class Person:
    def __init__(self, name):
        self.name = name

    # Define a method
    def say_hello(self, to_name=None):
        if to_name is not None:
            return greet(to_name)
        else:
            return "Hello World!"

def main():
    # Create an instance of the Person class
    alice = Person("Alice")

    # Call the say_hello method without an argument
    print(alice.say_hello())

    # Call the say_hello method with an argument
    print(alice.say_hello("Bob"))

# This is known as the "entry point."  It checks whether this Python
# script is being run directly or else is imported as a module by another
# script. The "__name__" is called a "dunder variable" (for "double under") and
# it is a built-in Python variable that points to the
# current module.

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------
# There are other "dunder variables" in Python
# 
# __doc__: This variable contains the docstring of a module, class, or function. 
# It is the first statement in the definition and is enclosed in triple quotes (""" or ''').
# 
# __file__: This variable contains the path of the script file that is currently being executed. 
# When used in a module, it represents the file path of that module.
# 
# __package__: This variable contains the package name of the current script or module. 
# It is used to manage the organization and import of modules in a package.
# 
# __all__: This variable is a list that defines the public interface of a module. 
# When a client imports a module using a wildcard import (e.g., from module import *), 
# only the names listed in __all__ are imported. If __all__ is not defined in the module, 
# then the wildcard import will import all names that are defined in the module, except 
# those beginning with an underscore (_).
# 
# __version__: This variable is a convention used by many modules and packages to indicate 
# their version number. It is typically a string that represents the version in a human-readable 
# format.
# 
# 
