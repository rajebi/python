import numpy as np
import collections
from array import *

#Coding
# data structures in python; 
# personal learning purpose only.

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

    # begining till end
    Sliced_array = a[:]
    print("\nPrinting all elements using slice operation: ")
    print(Sliced_array)

#============ List ========================
def list_examples():
    print("========= List basics ===============");
    lst1 = ['atlanta', 'newyork', 290, 400]
    lst2 = [1, 2, 3, 4, 5 ]
    lst3 = ["a", "b", "c", "d"]

    print ("lst1[0]: ", lst1[0])
    print ("lst2[1:5]: ", lst2[1:5])

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
    for x in [1, 2, 3, 4, 5, 6]: print(x, end =" ")  # pint in the same line.

    #comprehension
    a = [i for i in range(1,5)]
    print (a)

    a = [i+i for i in range(5)]
    print (a)

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

#================== Tuples ===========================
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

    tup1 = ();  # empty tuple
    tup1 = (50,); # tuple with single value.

    #updating typle
    # tup1[0] = "flight"  # this is not valid because tuple are immutable.
    # So let's create a new tuple as follows
    tup4 = tup1 + tup2;
    print (tup4);

    # basic tuple operations
    ln = len((1, 2, 3))	# 3	Length
    tup5 = (1, 2, 3) + (4, 5, 6) #	(1, 2, 3, 4, 5, 6)	Concatenation
    tup7 = ('same!',) * 4	# ("same" "same", ...) Repetition
    print(3 in (1, 2, 3))	# True	Membership
    for x in (100, 200, 300): print (x) #	1 2 3	Iteration

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

#==================== Set ============================
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

#==================== maps ==========================
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

#=============== advanced operations =================
def adv_operations():
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



# numpy examples

# testing
list_examples()
