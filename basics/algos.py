from typing import List
from os.path import join

#================ kth largest in an array =====================
# find the kth largest element in an array
# we use partioning technique to solve this problem. 
# Note if we taken sort and find the kth element, the kth largest would be at n-k th position. 
# in this case n - k = 7. (where n = 10, k = 3)
class KthLrgest:
    def __init__(self):
        print("init")    
    
    # solution 1, simple sorting
    def sort_and_find(self, l : List[int], k: int) -> int:
        l.sort()
        return l[len(l) - k]

    # solution 2 using partition method
    def partion_and_find(self, a : List[int], k: int) -> int:
        k = len(a)-k; # kth largest's index
        print(" the kth value is at = ", len(a) - k)

        def quick_select(l, r)-> int:
            pivot = a[r]
            #print (l)
            for i in range(l, r-1):
                if(a[i] < pivot): 
                    a[i] , a[l] = a[l], a[i] # swap the l and the current index
                    l = l+1 # move the left index

            # swap the pivot and the last element of the left partition.
            a[r] , a[l] = a[l], a[r] 
            print(a[l:r])
            print("l = ", l, "r = ", r)
            
            if(l < k): print("1", a[l+1:r]); return quick_select(l+1, r); 
            elif(l > k): print("2", a[k:l]); return quick_select(k,l-1); 
            else: print(" kth largest = ", a[k]); return a[k]
        
        return quick_select(0, len(a)-1)

b = [8, 2, 10, 4, 7, 5, 1, 3, 9, 6] ; m = 4
sol = KthLrgest()
print ("kth lrgest = ", sol.partion_and_find(b, m))  # print the 4th largest using sort and find method
print(b) # note b's content is changed, since it is a list. So it is pass by reference by default.


#==================== recursion examples ======================
def get_input():
    my_var = input('Enter "a" or "b": ')

    if my_var != "a" and my_var != "b":
        print('You didn\'t type "a" or "b". Try again.')
        return get_input()
    else:
        return my_var
#print('got input:', get_input())

# reverse elements in a list
def reverse_elements(s):
    r = len(s)-1

    def reverse(l:int, r:int):
        s[l], s[r] = s[r], s[l]
        l = l + 1; r = r - 1
        if( l < r): return reverse (l, r)
        else: return s
    
    return reverse(0, r)

c = [8, 2, 10, 4, 7, 5, 1, 3, 9, 6]
print( "reversed elements = ", reverse_elements(c))

# reverse a string
def reverse_string(st):
    r = len(st)-1
    # string type is immutable, hence the cannot be changed. Need to convert it to 
    # list then convert back.
    s = list(st) 
    def reverse(l:int, r:int):
        s[l], s[r] = s[r], s[l]
        l = l + 1; r = r - 1
        if( l < r): return reverse (l, r)
        else: return ''.join(s)
    
    return reverse(0, r)
s = input('enter a string ')
print( "reversed elements = ", reverse_string(s))

#================ heapify recursion =========================

