"""
Sorted Squared Array - 
You are given an array of Integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
""" 
#Brute force method
# Time = O(nlogn)  Space = O(n)
def sorted_squared(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        # new_array[i] = array[i]*array[i]
    new_array.sort()
    return new_array
#def square_and_sort(arr):
#    return sorted([num**2 for num in arr])
    
# Time = O(n) Space = O(n)
def sorted_squared(array):
    i = 0
    j = len(array) - 1
    new_array = [0] * len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j = array[j]** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array    