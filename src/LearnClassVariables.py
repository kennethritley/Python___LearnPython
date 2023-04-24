'''
PythonThis module demonstrates the usage of global, local, instance, and class variables
in Python through a simple "Hello World" application that includes a Person class.
Ich möchte mich bei meinem KI-Freund und Kupferstecher herzlich bedanken.

Author: KEN
Date:   2023.04.23
'''

# ***** GLOBAL VARIABLE *****
# This variable can be accessed everyone in the script!
greeting = "Hello"

# Define a function to demonstrate local variables
def greet(name):
    # NOTE: Because "greeting" is a global variable, you can access
    # it here. But if you wanted to change its value, you would need:
    # "global greeting" as a command here. That is needed to change g-variables!
    # *****LOCAL VARIABLE *****
    # This variable can only be accessed in this function
    punctuation = "!"
    return f"{greeting}, {name}{punctuation}"

# Define a class
class Person:
    # ***** CLASS VARIABLE *****
    # This variable will be available to all instances of the class.
    # If any one instance changes this variable, all other instances of 
    # this class will see those changes!  VERY COOL!
    default_name = "Anonymous"

    def __init__(self, name=None):
        if name is None:
            name = Person.default_name
        # ***** INSTANCE VARIABLE *****
        # This variable has a scope that is restricted to each instance of
        # the class, i.e. if you change the variable in an instance, no other
        # instance can see those changes
        self.name = name

    # Define a method
    def say_hello(self, to_name=None):
        if to_name is not None:
            return greet(to_name)
        else:
            return f"{greeting} World!"

def main():
    # Create instances of the Person class
    alice = Person("Alice")
    bob = Person("Bob")

    # Call the say_hello method without an argument
    print(alice.say_hello())

    # Call the say_hello method with an argument
    print(alice.say_hello(bob.name))

    # Change the class variable
    Person.default_name = "New Default"

    # Create a new instance of the Person class without specifying a name
    new_person = Person()

    # The new instance will use the updated default_name class variable
    print(new_person.say_hello())

if __name__ == "__main__":
    main()
