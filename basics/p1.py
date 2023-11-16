import numpy as np
import collections
from array import *

#Coding
# data structures in python; 
# personal learning purpose only.

def basic_types():
    # we can assign two variable on the same line
    m, n, f, b = 20, "string", 30.12, True

    print(m, n, f, b)

    # python has NULL, its called None.
    val = 50
    val = None
    print(val)

    if m < f:
        print ("test if") 
    
    for i in range(5): print(i, end=" ") # goes from 0 to 4
    print()
    for i in range(1, 5): print(i, end=" ")  # goes from 0 to 5
    print()
    for i in range(5, 1, -1): print(i, end=" ")  # goes from 5 to 2

    # flot and integer answers on division. 
    print(7/2, end=" "); print(7//2, end=" ")
    # -ve division
    print(-7/2, end=" "); print(-7//2, end=" ") ; # rownd downs to -4 in 7//2
    # workaround to round up -ve integer division
    print(int(-7/2), end=" ")
    print()
    # modulo
    print (20 % 7, end= " "); 
    print (-20 % 8, end= " ");  # -ve mod is undefined in python, it would give 16+8 - 20 = 4
    print()
    import math
    print (math.fmod(-20, 7), end= " ");
    #math functions
    print(math.floor(20/7), end=" "); print(math.ceil(20/7), end=" ");
    print(math.sqrt(25), end=" "); print(math.pow(6,2), end=" ");print()

    # infinity
    print(math.pow(3,100) < float("inf"))

    #string
    s = "abcdefg" ; # string is immutable
    #s[0] = "d" # will give an error.
    s = s + "h"; print(s) # this will create a new string s
    print(s[2:5])
    # integer to string and vice versa operations
    print(int("500") + int("200"))
    print(str(500) + str(200))
    #ascii value
    print(ord("a"))
    s = ["11", "aa", "zz"]
    print(" ".join(s)) # here single space is used as delimiter to join the string
    print("".join(s)) # here no space is used as delimiter to join the string
    print(":".join(s)) # here :  is used as delimiter to join the string


#======================== arrays ==============
def array_examples():
    a = array('i', [1,22,3,44,55]) # "i" here means array with integer type
    b = array('d', [2.5, 3.2, 3.3]) # float type
    b.append(4.4) # will append at the end.

    for x in a:
        print (x)
    # print a location
    print (a[0]); print (a[2])
    # insertion
    a.insert(1, 65); print (a)
    # deletion
    a.remove(65); print (a)
    #search index
    print (a.index(44))
    #update
    a[2] = 8; print (a)

    #slicing array
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list
    a = array('i', l)
    Sliced_array = a[3:8]
    print("\nSlicing elements in a range 3-8: ")
    print(Sliced_array)

    # beginning till end
    Sliced_array = a[:]
    print("\nPrinting all elements using slice operation: ")
    print(Sliced_array)

#============ List ========================
# array in python are defined as Lists.
def list_examples():
    print("========= List basics ===============");
    lst1 = ['atlanta', 'newyork', 290, 400]
    lst2 = [1, 2, 3, 4, 5 ]
    lst3 = ["a", "b", "c", "d"]

    print ("lst1[0]: ", lst1[0])
    print ("lst2[1:5]: ", lst2[1:5])

    # append, push and pop.
    lst2.append(6); print(lst2)
    lst2.pop(); print(lst2)
    lst2.insert(4,7); print(lst2)

    #-ve index; reads from the last
    a = [1, 2, 3, 4, 5 ]
    print(a[-1]) # will print 5
    print(a[-4]) # will print 2

    #slicing
    print(a[1:4]) # will print from index 1 to 3, exclusing 4
    i , j , k = [10, 20, 30] # will assing i = 10, j = 20, k = 30

    # looping:  3 ways
    for i in range(len(a)): print(a[i], end=" "); print()
    for i in a: print(i, end=" "); print()
    for i, n in enumerate(a): print(i, n, end=" "); print() # will print both index and value.

    a = [1, 2, 3, 4, 5 ]; b = [-1, -2, -3, -4, -5 ]
    for m, n in zip(a, b): print(m, n, end=" "); print() # will prints values from both the arrays

    # reverse 
    a = [1, 2, 3, 4, 5 ]; b = [-1, -2, -3, -4, -5 ]
    a.reverse(); print("reverse = ", a)
    # sorting
    b.sort(); print("sort ",b)
    # sort in descending order
    a = [1, 2, 3, 4, 5 ]
    a.sort(reverse=True); print("reverse ", a); 
    # sorting string
    s = ["apple", "bat", "cat", "donkey"]
    s.sort(); print(s)
    # sorting using a length of the strings
    s = ["apple", "bat", "cat", "donkey"]    
    s.sort(key=lambda x:len(x)); print(s) # lambda is an empry function which is defined as x:len(x)

    #comprehension
    a = [i for i in range(1,5)]
    print (a)

    a = [i+i for i in range(5)]
    print (a)

    a = [[1] * 3 for i in range(4)]
    print("list = ", a)

    a = [[1] * 3] * 4 
    print("list = ", a)

    # updating list
    lst2[0] = 10
    print (lst2[0])

    del lst2[0]
    print(lst2)

    # basic list operations
    print("length of list = ", len([1, 2, 3, 4])) # length = 4 here
    lst_concat = [10, 20, 30] + [40, 50, 60] ; print (lst_concat)
    lst_repeat = ['same!'] * 5; print (lst_repeat)
    print( 30 in [11, 22, 30] )
    for x in [1, 2, 3, 4, 5, 6]: print(x, end =" ")  # print in the same line.
   
    # iterating in list; this will create list of even number from 0 to 1000
    lst = [i for i in range(0,1000) if i % 2 == 0]

    # example : notmal way
    def times_tables():
        lst = []
        for i in range(10):
            for j in range (10):
                lst.append(i*j)
        return lst

    print("times tables : ", times_tables())
    # list comprehension - short method	
    #times_tables == [i*j for i in range(1,2) for j in range(1,2)]
    t_tables = [i*j for i in range(1,6) for j in range(1,6)]
    print("t tables : ", t_tables)

    # example for short cut methonds
    # Many organizations have user ids which are constrained in some way. 
    # Imagine you work at an internet service provider and the user ids are all two 
    # letters followed by two numbers (e.g. aa49). Your task at such an organization might
    # be to hold a record on the billing activity for each possible user.

    # Write an initialization line as a single list comprehension which creates a list of 
    # all possible user ids. Assume the letters are all lower case.

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
    correct_answer[:50] # Display first 50 ids
    print(correct_answer[:5])

#==================== HashSets ============================
# Mathematically a set is a collection of items not in any particular order. 
# A Python set is similar to this mathematical definition with below additional conditions.
#   The elements in the set cannot be duplicates.
#   The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
#   There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

# The sets in python are typically used for mathematical operations like union, 
# intersection, difference and complement etc. We can create a set, access it’s elements 
# and carry out these mathematical operations as shown below.

def set_examples():
    # creating set
    Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
    Months={"Jan","Feb","Mar"}
    Dates={21,22,17}
    print(Days); print(Months); print(Dates)

    # another way to create set
    s = set()
    s.add(1); s.add(2); s.add(3);
    print("hash set s = ", s)
    print(1 in s); # will print True
    print(4 in s) # print False

    # remove value
    s.remove(2)

    # another way to initialize hash set
    s = set([i for i in range(5)]); print(s)
    s = {i for i in range(5,10)}; print(s)

    # Hash map : used for hashing. This is basically dictionary in python.
    hashmap = {}
    hashmap["a"] = 10; hashmap["b"] = 20; hashmap["c"] = 30
    print("hashmap = ", hashmap); print("len of hashmap = ", len(hashmap))

    hashmap1 = {}
    hashmap1["d","e","f"] = {40, 50, 60}
    print("hashmap1 = ", hashmap1); print("len of hashmap1 = ", len(hashmap1))
    #print(hashmap1["d"]) # this will give key error
    print(hashmap1["d", "e", "f"]) # this will pring {40, 50, 60}

    # we can change the value for a key
    hashmap["a"] = 100; print(hashmap)
    # we can remove a key, this will also remove the value
    hashmap.pop("b"); print(hashmap)

    # another way to initialize.
    hashmap = {"i" : 100, "j" : 200, 'k': 300} 

    # dictionaly comprehension
    k = 10
    hashmap = {j : 3 * j for j in range(1,5)}
    print("hashmap comprehension :", hashmap)

    # creating hash value from a function call
    import random
    def foo():
        return round(random.random(), 2)
    hashmap = {j : foo() for j in range(1,5)}
    print("hashmap comprehension :", hashmap)

    # creating key and value from function
    def goo():      # goo() is key, foo() is value
        return [10, 20, 30]
    hashmap = {j : foo() for j in goo()}
    print("hashmap comprehension :", hashmap)

    # hashmaps (dict) are used in graph problems where we can create mapping between
    # node and links

    # printing key and val
    for key in hashmap:
        print(k, hashmap[key])
    
    for val in hashmap.values():
        print(val)
    
    for key, val in hashmap.items():
        print(key, val)

    print(hashmap.items()); # prints key value pair
    print(hashmap.values()); 
    print(hashmap.keys()); 


    # accessing set
    for d in Days:
        print(d)

    # adding item to set
    Days.add("Sun"); print(Days)
    # removing from a set
    Days.discard("Sun"); print(Days)
    # union of sets
    DaysA = set(["Mon","Tue","Wed"])
    DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
    AllDays = DaysA | DaysB;  # union operation
    print(AllDays)
    # intersection of sets
    AllDays = DaysA & DaysB; print(AllDays)

    # difference of sets
    AllDays = DaysA - DaysB ; print(AllDays)

    # Compare 2 sets
    SubsetRes = DaysA <= DaysB
    SupersetRes = DaysB >= DaysA
    print(SubsetRes)    # answer will be True or false. In this case True.
    print(SupersetRes)

#==================== Dictionary ==========================================
# In Dictionary each key is separated from its value by a colon (:), 
# the items are separated by commas, and the whole thing is enclosed in curly braces. 
# An empty dictionary without any items is written with just two curly braces, like this − {}.
# Keys are unique within a dictionary while values may not be. The values of a dictionary 
# can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

def dictionary_examples():
    # key as string
    dict = {'Name': 'sam', 'Age': 9, 'Class': '3rd'}
    print ("dict['Name']: ", dict['Name'])
    print ("dict['Age']: ", dict['Age'])

    # updating
    dict['Age'] = 8; # update existing entry
    dict['School'] = "public school"; # Add new entry

    # deleting 
    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary

    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])

    # More than one entry per key not allowed. Which means no duplicate key 
    # is allowed. When duplicate keys encountered during assignment, the last assignment wins.
    dict = {'Name': 'sam', 'Age': 8, 'Name': 'jim'}
    print ("dict['Name']: ", dict['Name'])

    # key as integer
    dict2 = { 1: 10, 2:20, 3:30}
    print("dict2[1] = ", dict2[1])

    # key as tuple
    dict3 = { (1,2,3): 10, (10,20,30):20, (1,2,3):30}
    print("dict3[(1,2,3)] = ", dict3[(1,2,3)])
    print("dict3[(10,20,30)] = ", dict3[(10,20,30)])


#================== Tuples =======================================
# A tuple is a sequence of immutable Python objects. 
# Tuples are sequences, just like lists. The differences between 
# tuples and lists are, the tuples cannot be changed unlike lists 
# and tuples use parentheses, whereas lists use square brackets.
def tuple_examples():
    print("========= tuple basics ===============");
    tup1 = ('car', 'bus', 97, 20);
    tup2 = (1, 2, 3, 4, 5 );
    tup3 = "a", "b", "c", "d";

    print ("tup1[0]: ", tup1[0])
    print ("tup2[1:5]: ", tup2[1:5])
    print("tup2[-1]", tup2[-1]) # this will print the last element, similar to list

    tup1 = ();  # empty tuple
    tup1 = (50,); # tuple with single value.

    # updating typle
    # tup1[0] = "flight"  # this is not valid because tuple are immutable.
    # So let's create a new tuple as follows
    tup4 = tup1 + tup2;
    print (tup4);

    # tuples can be used as keys for hashmaps/dictionaries. This is the reason
    # tuples are immutable as keys cannot be changed. We cannot use list as a key.
    t1 = (1, 2); t2 = (3, 4)
    hashmap = {t1 : "a", t2 : "b"}
    print("hashmap with tuple as keys: ", hashmap)

    # basic tuple operations
    ln = len((1, 2, 3))	# 3	Length
    tup5 = (1, 2, 3) + (4, 5, 6) #	(1, 2, 3, 4, 5, 6)	Concatenation
    tup7 = ('same!',) * 4	# ("same" "same", ...) Repetition
    print(3 in (1, 2, 3))	# True	Membership
    for x in (100, 200, 300): print (x) #	1 2 3	Iteration

#===================== 2-D array ======================
def Two_D_array_examples():
    print("2D array examples")
    T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
    print(T[0])
    print(T[1][2])
    print(T)

    for r in T:
        for c in r:
            print(c,end = " ")
    print()

    # inserting
    T.insert(2, [0,5,11,13,6])
    print(T)

    # updating
    T[2] = [11,9]
    T[0][3] = 7
    print(T)

    #deleting
    del T[3]
    print(T)

#==================== Matrix ==========================
def matrix_examples():
    a = [['Mon',18,20,22,17],['Tue',11,18,21,18],
            ['Wed',15,21,20,19],['Thu',11,20,22,21],
            ['Fri',18,17,23,22],['Sat',12,22,20,18],['Sun',13,15,19,16]]         

    m = np.reshape(a,(7,5))
    print(m)

    # accessing 
    print(m[2])
    # Print data for friday evening
    print(m[4][3])

    # adding a row
    m_r = np.append(m,[['Avg',12,15,13,11]],0)
    print(m_r)

    # transpose matrix
    m_transpose = np.reshape(a,(5,7))
    print(m_transpose)


#==================== maps ===================================================
# Python Maps also called ChainMap is a type of data structure to
# manage multiple dictionaries together as one unit. The combined dictionary 
# contains the key and value pairs in a specific sequence eliminating any 
# duplicate keys. The best use of ChainMap is to search through multiple dictionaries 
# at a time and get the proper key-value pair mapping. We also see that these 
# ChainMaps behave as stack data structure.
def maps_examples():
    print("============ maps =================")

    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    res = collections.ChainMap(dict1, dict2)

    # Creating a single dictionary
    print(res.maps,'\n')

    # format() in python formats the specified value(s) and insert them 
    # inside the string's placeholder. The place holder is defined using {}
    print('Keys = {}'.format(list(res.keys())))  
    print('Values = {}'.format(list(res.values())))
    print()

    # Print all the elements from the result
    print('elements:')
    for key, val in res.items():
        print('{} = {}'.format(key, val))
        print()

    # Find a specific value in the result
    print('day3 in res: {}'.format(('day1' in res)))
    print('day4 in res: {}'.format(('day4' in res)))

    # --- Map reordering -------
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day4': 'Thu'}

    res1 = collections.ChainMap(dict1, dict2)
    print(res1.maps,'\n')

    res2 = collections.ChainMap(dict2, dict1)
    print(res2.maps,'\n')

    # updating map
    dict2['day4'] = 'Fri' ; print(res.maps,'\n')

#=============== mist operations =================
def misc_operations():
    # string split and mapping
    people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

    def split_title_and_lastname(person):
        title = person.split()[0]
        lastname = person.split()[-1]
        return '{} {}'.format(title, lastname)

    lst4 = list(map(split_title_and_lastname, people))
    print (lst4)

    def split_title_and_firstname(person):
        title = person.split()[0]
        firstname = person.split()[-2]
        return '{} {}'.format(title, firstname)

    lst5 = list(map(split_title_and_firstname, people))
    print (lst5)

    def split_title_and_lname(person):
        return person.split()[0] + ' ' + person.split()[-1]

    #lst6 = list(map(split_title_and_lname, people))
    #print(lst6)

    #option 1
    #for person in people:
    #    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

    #option 2
    list(map(split_title_and_lname, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

#================ Queues ====================
def queue_examples():
    from collections import deque

    # queue in python is double ended, we can add or remove on both side.
    q = deque()
    q.append(10); 
    q.append("b"); # adding on the right
    print(q)
    q.popleft(); print(q)  # popping on the left
    
    q.appendleft(10); print(q) # addinig on the left
    q.pop(); print(q) # removing on the right

#================== heap ====================================================
# in python heap is implemented as list
# by default it is implemented as minheap. That means the top most is the lowest value.

def heap_examples():
    import heapq

    h = [] # basically a list
    heapq.heappush(h, 30)
    heapq.heappush(h, 20)
    heapq.heappush(h, 10)

    print(h); print(h[0], h[1], h[2]); 

    # note if we do heappop, it will come in ascending order.
    # the minimum will be popped first

    while len(h):
        print(heapq.heappop(h), end=" ")

    print()
    # python does not have max heap by default. workworund is to multiple each value
    # by -1 and push, then pop & multiply -1.
    heapq.heappush(h, -30)
    heapq.heappush(h, -20)
    heapq.heappush(h, -10)

    while len(h):
        print(heapq.heappop(h) * -1, end=" ")
    print()
    # constructing heap frmo a list
    lst = [8, 2, 10, 4, 7, 5, 1, 3, 9, 6]
    heapq.heapify(lst)
    while len(lst):
        print(heapq.heappop(lst), end=" ")

    # To find kth largest value from the list
    b = [8, 2, 10, 4, 7, 5, 1, 3, 9, 6]
    heapq.heapify(b)
    k = 4; i = 0;
    while len(b):
        heapq.heappop(b);
        if(len(b)-k == 0):
            print("kth largest = ", heapq.heappop(b))
            break

#================= functions ========================

#example of nonlocal used in nested function.
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
#basic_types()
#list_examples()
#queue_examples()
#set_examples()
#tuple_examples()
#heap_examples()
function_test()
