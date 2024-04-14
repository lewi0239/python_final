"""
What are Tuples?

Author: Python documentation
Title: 5. Data Structures - Tuples and Sequences
Code Version: Python 3
Type: Documentation
Link: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

Tuples are ordered, indexed collections of data. Similar to string indices, the first value in the tuple will have the index [0], the second value [1], and so on.
"""

# Create a tuple of student names!
student_tuple = "brodie", "mike", "ashlee", "tom"
print(student_tuple)  # prints names listed above in console

# Create a tuple with three numbers inside it
num_tuple = (10, 100, 100)
print(num_tuple)  # print numbers listed above

# square each index and add
num_tuple = num_tuple[1] ** 2 + num_tuple[0] ** 2 + num_tuple[2] ** 2

print(num_tuple)  # print simple expression, expected result 20100

# simple tuple with different cup sizes
cup_sizes = "small", "large", "medium"
print(len(cup_sizes))  # expected result = 3

"""
How does tule allow negative indexing?

Title: 5. Data Structures - More on Lists
Code Version: Python 3
Type: Documentation
Link: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Use negative indexes to start the slice from the end of the string, where -1 is the last index
"""
# simple object that equals a string
b = "Hello World!"
print(b[-6:-1])  # slice word down to World

# simpel tuple equals a list of numbers
a = 1, 2, 3, 4, 5, 6

print(a[-3:-1])  # will print 4, 5 in console

"""
How does deleting work in a tuple?

Title: 2. Lexical analysis - Parenthesized forms
Code Version: Python 3
Type: Documentation
Link: https://docs.python.org/3/reference/expressions.html#parenthesized-forms

The del keyword is mostly used in Python to delete objects. Because everything in Python is an object, the del keyword can be used to delete a tuple, slice a tuple, delete dictionaries, remove key-value pairs from a dictionary, delete variables, and so on.
"""

# tuple with different objects inside it
tuple_del = "tutorials", "point", 2022, True
print(tuple_del)  # print tuple above in console
new_tuple = tuple_del[:1] + tuple_del[3:]  # deletes point and 2022

print(new_tuple)  # print results in console
