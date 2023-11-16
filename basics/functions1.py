import numpy as np
import collections
from array import *

#Coding
# data structures in python; 
# personal learning purpose only.

#================= functions ========================

# example of nonlocal used in nested function.
# nonlocal helps in accessing the variable in the upper scope.
# The nonlocal keyword can only be used inside nested structures.
def goo(num, val, val2):
    def foo():
        # modifying num which is list, will also modify the original array passed in
        for i, n in enumerate(num):
            num[i] = i * 4
        nonlocal val  # to make val's scope to global within goo() level, nonlocal declaration is needed
        val = 500
        val2 = 600
    foo()
    print("goo-f", num, val, val2)

def hoo(num, val, val2):
    def foo():
        # modifying num which is list, will also modify the original array passed in
        for i, n in enumerate(num):
            num[i] = i * 3
        val = 5  # val changed inside the foo()'s scope only. "val" will be a local variable inside foo()
    foo()
    print("hoo-f", num, val)

# counter function
def counter():
    c = 0 # Local counter variable
   
    # This function manipulate the
    # local c variable, when called
    def count():
        nonlocal c
        c += 1
        return c
   
    # Return the count() function to manipulate
    # the local c variable on every call
    return count

def nonlocal_test(): 
    # Assign the result of counter() to
    # a variable which we use to count up
    m_counter = counter()
    for i in range(3):
        print(m_counter(), end=" ")
    print('\nEnd of m_counter')
    
    # Create a new counter
    n_counter = counter()
    for i in range(3):
        print(n_counter(), end=" ")
    print('\nEnd of n_counter')

def try_to_modify(l):
    l = [5, 6, 6] # this does not change the content of the list passed in.

def modify_list(l):
    l[0], l[1]  = 5, 6  # this will change the content.

def append_list(l):
    l.append(5); l.append(6); l.append(7)

def set_list(list):
    list = ["A", "B", "C"]
    return list
 
def add_list(list):
    list.append("D")
    return list

def function_test():

    # In python the aruments are name of the reference of the objects. They are not 
    # same as pass by reference in C. when a function is called an identifier is bound to the 
    # actual object passed in.   
    # An entry is added in the current namespace to bind the identifier "l" to 
    # the object representing list. This entry is in fact a key-value pair stored in a dictionary! 
    # A representation of that dictionary is returned by locals() or globals().
    # Until the identifier used in an assignment, it will still point to the original object. 
    # read geeks or https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/ 
    # https://realpython.com/python-pass-by-reference/
    # 

    l = [1,2]
    try_to_modify(l)
    # here the content of l is not changed. 
    # because when l is assgined in create_list() the local l there points to different object [5, 6, 7]
    print("try modify list = ", l) 
    
    modify_list(l) # this will change the content because l is not assigned in the function.
    print("modify list = ", l) 

    l = []
    try_to_modify(l); print(l) # this will print None
    append_list(l); print(l) # this will print new values

    # example shows why l is not changed by the set_list(), but changed by add. 
    l = ["E"]
    print(set_list(l)); print(l)
    print(add_list(l)); print(l)
    
    gnum = [1, 2, 3]
    val, val2 = 1, 2
    goo(gnum, val, val2)
    print ("goo", gnum, val, val2)
    hoo(gnum, val, val2)
    print ("hoo", gnum, val, val2)
    nonlocal_test()
    

# numpy examples

# testing
function_test()
