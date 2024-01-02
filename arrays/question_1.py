""" 
Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
"""

def sorted_squared_array(my_array):
    squared_array = []

    for number in my_array:
        squared_array.append(number **2)

    # Sort the squared array   
    squared_array.sort()

    return squared_array

sorted_squared_array([2,3,7,1])